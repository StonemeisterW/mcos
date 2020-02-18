import pytest

from mcos.covariance_transformer import CovarianceMatrixDeNoiser
from numpy.testing import assert_almost_equal
from pypfopt.risk_models import sample_cov


class TestCovarianceMatrixDeNoiser:
    def test_transform(self, prices_df, de_noised_covariance_matrix_results):
        covariance_matrix = sample_cov(prices_df).values
        n_observations = prices_df.size
        results = CovarianceMatrixDeNoiser().transform(covariance_matrix, n_observations)
        assert results.shape == (20, 20)
        assert_almost_equal(results, de_noised_covariance_matrix_results)


@pytest.fixture
def de_noised_covariance_matrix_results():
    return [[0.09321114, 0.03793818, 0.02756239, 0.02721393, 0.04944894, 0.03042882,
             0.05567555, 0.01805353, 0.04697079, 0.02741789, 0.02005035, 0.05089275,
             0.04342173, 0.02325903, 0.04146274, 0.03610952, 0.03926564, 0.02341933,
             0.0417671, 0.0349097],
            [0.03793818, 0.20753691, 0.03114646, 0.02965087, 0.08158306, 0.03562814,
             0.07820231, 0.02697621, 0.05038849, 0.02672283, 0.02025689, 0.05715915,
             0.05184438, 0.01897616, 0.02776881, 0.06187122, 0.04115407, 0.02421112,
             0.0479363, 0.04886798],
            [0.02756239, 0.03114646, 0.13720115, 0.03295926, 0.03954143, 0.0140821,
             0.04975629, 0.00335246, 0.0240672, 0.0181963, 0.00501589, 0.03252855,
             0.01981124, 0.01264117, 0.02936493, 0.01963741, 0.02355954, 0.00897232,
             0.02006967, 0.02113086],
            [0.02721393, 0.02965087, 0.03295926, 0.10095819, 0.03755445, 0.01577825,
             0.04713898, 0.00510145, 0.02643904, 0.01885181, 0.00719787, 0.03360924,
             0.02223839, 0.01397838, 0.03063408, 0.02000447, 0.02487117, 0.01083839,
             0.02229337, 0.02161166],
            [0.04944894, 0.08158306, 0.03954143, 0.03755445, 0.37539405, 0.04805009,
             0.10642251, 0.03827507, 0.06661261, 0.03421156, 0.02692804, 0.07565924,
             0.07019209, 0.02339739, 0.03142033, 0.08796492, 0.05382226, 0.03204046,
             0.06434402, 0.06739957],
            [0.03042882, 0.03562814, 0.0140821, 0.01577825, 0.04805009, 0.08310901,
             0.04797671, 0.02498078, 0.0505692, 0.02608308, 0.02512856, 0.0506238,
             0.04940866, 0.02348223, 0.03591982, 0.04209481, 0.03964437, 0.02721981,
             0.04646439, 0.03725377],
            [0.05567555, 0.07820231, 0.04975629, 0.04713898, 0.10642251, 0.04797671,
             0.39058571, 0.03261613, 0.07027247, 0.03968584, 0.0271167, 0.08068112,
             0.06935687, 0.02916663, 0.04820016, 0.07706166, 0.05887654, 0.03319143,
             0.06513777, 0.06444232],
            [0.01805353, 0.02697621, 0.00335246, 0.00510145, 0.03827507, 0.02498078,
             0.03261613, 0.06909179, 0.03457652, 0.01563706, 0.0183678, 0.03351023,
             0.03633702, 0.0137844, 0.01633393, 0.03636691, 0.02571728, 0.01922896,
             0.03325242, 0.02839109],
            [0.04697079, 0.05038849, 0.0240672, 0.02643904, 0.06661261, 0.0505692,
             0.07027247, 0.03457652, 0.18019232, 0.04052177, 0.03728307, 0.07630861,
             0.07241617, 0.03698499, 0.05967187, 0.05715468, 0.06031759, 0.04066822,
             0.06873606, 0.05335959],
            [0.02741789, 0.02672283, 0.0181963, 0.01885181, 0.03421156, 0.02608308,
             0.03968584, 0.01563706, 0.04052177, 0.08011557, 0.01877585, 0.04190931,
             0.03711057, 0.02095075, 0.03678836, 0.02678378, 0.03322378, 0.02108901,
             0.03579643, 0.02731949],
            [0.02005035, 0.02025689, 0.00501589, 0.00719787, 0.02692804, 0.02512856,
             0.0271167, 0.0183678, 0.03728307, 0.01877585, 0.06555993, 0.03537568,
             0.0360173, 0.01824595, 0.0276976, 0.02652113, 0.02861946, 0.02092877,
             0.03398571, 0.02462412],
            [0.05089275, 0.05715915, 0.03252855, 0.03360924, 0.07565924, 0.0506238,
             0.08068112, 0.03351023, 0.07630861, 0.04190931, 0.03537568, 0.24552417,
             0.07251432, 0.03669347, 0.0608872, 0.06068954, 0.06175161, 0.03963838,
             0.06896087, 0.0562107],
            [0.04342173, 0.05184438, 0.01981124, 0.02223839, 0.07019209, 0.04940866,
             0.06935687, 0.03633702, 0.07241617, 0.03711057, 0.0360173, 0.07251432,
             0.32116207, 0.03326289, 0.05029665, 0.06161128, 0.05664559, 0.03898697,
             0.06674795, 0.05395087],
            [0.02325903, 0.01897616, 0.01264117, 0.01397838, 0.02339739, 0.02348223,
             0.02916663, 0.0137844, 0.03698499, 0.02095075, 0.01824595, 0.03669347,
             0.03326289, 0.05440377, 0.03544695, 0.019814, 0.02994191, 0.01992357,
             0.03229057, 0.0222057],
            [0.04146274, 0.02776881, 0.02936493, 0.03063408, 0.03142033, 0.03591982,
             0.04820016, 0.01633393, 0.05967187, 0.03678836, 0.0276976, 0.0608872,
             0.05029665, 0.03544695, 0.27222973, 0.02231614, 0.0502317, 0.03122642,
             0.05014523, 0.03223164],
            [0.03610952, 0.06187122, 0.01963741, 0.02000447, 0.08796492, 0.04209481,
             0.07706166, 0.03636691, 0.05715468, 0.02678378, 0.02652113, 0.06068954,
             0.06161128, 0.019814, 0.02231614, 0.26954874, 0.04400554, 0.02946496,
             0.05595612, 0.05536054],
            [0.03926564, 0.04115407, 0.02355954, 0.02487117, 0.05382226, 0.03964437,
             0.05887654, 0.02571728, 0.06031759, 0.03322378, 0.02861946, 0.06175161,
             0.05664559, 0.02994191, 0.0502317, 0.04400554, 0.12030304, 0.03174216,
             0.0540994, 0.04224545],
            [0.02341933, 0.02421112, 0.00897232, 0.01083839, 0.03204046, 0.02721981,
             0.03319143, 0.01922896, 0.04066822, 0.02108901, 0.02092877, 0.03963838,
             0.03898697, 0.01992357, 0.03122642, 0.02946496, 0.03174216, 0.08550166,
             0.03691128, 0.02754484],
            [0.0417671, 0.0479363, 0.02006967, 0.02229337, 0.06434402, 0.04646439,
             0.06513777, 0.03325242, 0.06873606, 0.03579643, 0.03398571, 0.06896087,
             0.06674795, 0.03229057, 0.05014523, 0.05595612, 0.0540994, 0.03691128,
             0.14689262, 0.0501378],
            [0.0349097, 0.04886798, 0.02113086, 0.02161166, 0.06739957, 0.03725377,
             0.06444232, 0.02839109, 0.05335959, 0.02731949, 0.02462412, 0.0562107,
             0.05395087, 0.0222057, 0.03223164, 0.05536054, 0.04224545, 0.02754484,
             0.0501378, 0.15258853]]
