import numpy as np
import pytest
from numpy.polynomial import Polynomial

import diffpy.morph.morphpy as morphpy
from diffpy.morph.morphapp import create_option_parser, single_morph
from diffpy.morph.morphs.morphsqueeze import MorphSqueeze
from tests.helper import create_morph_data_file

squeeze_coeffs_dic = [
    # The order of coefficients is {a0, a1, a2, ..., an}
    # Negative cubic squeeze coefficients
    {"a0": -0.01, "a1": -0.0005, "a2": -0.0005, "a3": -1e-6},
    # Positive cubic squeeze coefficients
    {"a0": 0.2, "a1": 0.01, "a2": 0.001, "a3": 0.0001},
    # Positive and negative cubic squeeze coefficients
    {"a0": 0.2, "a1": -0.01, "a2": 0.002, "a3": -0.0001},
    # Quadratic squeeze coefficients
    {"a0": -0.2, "a1": 0.005, "a2": -0.0004},
    # Linear squeeze coefficients
    {"a0": 0.1, "a1": 0.3},
    # 4th order squeeze coefficients
    {"a0": 0.2, "a1": -0.01, "a2": 0.001, "a3": -0.001, "a4": 0.0001},
    # Zeros and non-zeros, the full polynomial is applied
    {"a0": 0, "a1": 0.03, "a2": 0, "a3": -0.0001},
    # Testing zeros, expect no squeezing
    {"a0": 0, "a1": 0, "a2": 0, "a3": 0, "a4": 0, "a5": 0},
]
morph_target_grids = [
    # UCs from issue 181: https://github.com/diffpy/diffpy.morph/issues/181
    # UC2: Same range and same grid density
    (np.linspace(0, 10, 101), np.linspace(0, 10, 101)),
    # UC4: Target range wider than morph, same grid density
    (np.linspace(0, 10, 101), np.linspace(-2, 20, 221)),
    # UC6: Target range wider than morph, target grid density finer than morph
    (np.linspace(0, 10, 101), np.linspace(-2, 20, 421)),
    # UC8: Target range wider than morph, morph grid density finer than target
    (np.linspace(0, 10, 401), np.linspace(-2, 20, 200)),
    # UC10: Morph range starts and ends earlier than target, same grid density
    (np.linspace(-2, 10, 121), np.linspace(0, 20, 201)),
    # UC12: Morph range wider than target, same grid density
    (np.linspace(-2, 20, 201), np.linspace(0, 10, 101)),
]


@pytest.mark.parametrize("x_morph, x_target", morph_target_grids)
@pytest.mark.parametrize("squeeze_coeffs", squeeze_coeffs_dic)
def test_morphsqueeze(x_morph, x_target, squeeze_coeffs):
    y_target = np.sin(x_target)
    y_morph = np.sin(x_morph)
    # expected output
    y_morph_expected = y_morph
    x_morph_expected = x_morph
    x_target_expected = x_target
    y_target_expected = y_target
    # actual output
    coeffs = [squeeze_coeffs[f"a{i}"] for i in range(len(squeeze_coeffs))]
    squeeze_polynomial = Polynomial(coeffs)
    x_squeezed = x_morph + squeeze_polynomial(x_morph)
    y_morph = np.sin(x_squeezed)
    morph = MorphSqueeze()
    morph.squeeze = squeeze_coeffs
    x_morph_actual, y_morph_actual, x_target_actual, y_target_actual = morph(
        x_morph, y_morph, x_target, y_target
    )

    extrap_low = np.where(x_morph < min(x_squeezed))[0]
    extrap_high = np.where(x_morph > max(x_squeezed))[0]
    extrap_index_low_expected = extrap_low[-1] if extrap_low.size else 0
    extrap_index_high_expected = extrap_high[0] if extrap_high.size else -1

    extrapolation_info = morph.extrapolation_info
    extrap_index_low_actual = extrapolation_info["extrap_index_low"]
    extrap_index_high_actual = extrapolation_info["extrap_index_high"]

    assert np.allclose(
        y_morph_actual[
            extrap_index_low_expected + 1 : extrap_index_high_expected
        ],
        y_morph_expected[
            extrap_index_low_expected + 1 : extrap_index_high_expected
        ],
        atol=1e-6,
    )
    assert np.allclose(
        y_morph_actual[:extrap_index_low_expected],
        y_morph_expected[:extrap_index_low_expected],
        atol=1e-3,
    )
    assert np.allclose(
        y_morph_actual[extrap_index_high_expected:],
        y_morph_expected[extrap_index_high_expected:],
        atol=1e-3,
    )
    assert np.allclose(x_morph_actual, x_morph_expected)
    assert np.allclose(x_target_actual, x_target_expected)
    assert np.allclose(y_target_actual, y_target_expected)
    assert extrap_index_low_actual == extrap_index_low_expected
    assert extrap_index_high_actual == extrap_index_high_expected


@pytest.mark.parametrize(
    "squeeze_coeffs, wmsg_gen",
    [
        # extrapolate below
        (
            {"a0": 0.01},
            lambda x: (
                "Warning: points with grid value below "
                f"{x[0]} are extrapolated."
            ),
        ),
        # extrapolate above
        (
            {"a0": -0.01},
            lambda x: (
                "Warning: points with grid value above "
                f"{x[1]} are extrapolated."
            ),
        ),
        # extrapolate below and above
        (
            {"a0": 0.01, "a1": -0.002},
            lambda x: (
                "Warning: points with grid value below "
                f"{x[0]} and above {x[1]} are "
                "extrapolated."
            ),
        ),
    ],
)
def test_morphsqueeze_extrapolate(user_filesystem, squeeze_coeffs, wmsg_gen):
    x_morph = np.linspace(0, 10, 101)
    y_morph = np.sin(x_morph)
    x_target = x_morph.copy()
    y_target = y_morph.copy()
    morph = MorphSqueeze()
    morph.squeeze = squeeze_coeffs
    coeffs = [squeeze_coeffs[f"a{i}"] for i in range(len(squeeze_coeffs))]
    squeeze_polynomial = Polynomial(coeffs)
    x_squeezed = x_morph + squeeze_polynomial(x_morph)
    with pytest.warns() as w:
        morphpy.morph_arrays(
            np.array([x_morph, y_morph]).T,
            np.array([x_target, y_target]).T,
            squeeze=coeffs,
            apply=True,
        )
        assert len(w) == 1
        assert w[0].category is UserWarning
        actual_wmsg = str(w[0].message)
    expected_wmsg = wmsg_gen([min(x_squeezed), max(x_squeezed)])
    assert actual_wmsg == expected_wmsg

    # CLI test
    morph_file, target_file = create_morph_data_file(
        user_filesystem / "cwd_dir", x_morph, y_morph, x_target, y_target
    )

    parser = create_option_parser()
    (opts, pargs) = parser.parse_args(
        [
            "--squeeze",
            ",".join(map(str, coeffs)),
            f"{morph_file.as_posix()}",
            f"{target_file.as_posix()}",
            "--apply",
            "-n",
        ]
    )
    with pytest.warns(UserWarning, match=expected_wmsg):
        single_morph(parser, opts, pargs, stdout_flag=False)
