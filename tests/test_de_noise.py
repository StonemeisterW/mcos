from numpy.testing import assert_almost_equal
from pypfopt.risk_models import sample_cov
from mcos.de_noise import de_noise_covariance_matrix


def test_de_noise_covariance_matrix(prices_df, de_noised_covariance_matrix_results):
    covariance_matrix = sample_cov(prices_df).values
    n_observations = prices_df.size
    results = de_noise_covariance_matrix(covariance_matrix, n_observations=n_observations)
    assert results.shape == (20, 20)
    assert_almost_equal(results, de_noised_covariance_matrix_results)