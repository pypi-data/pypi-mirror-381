import pytest
import os
import dotenv
import redlistapi

dotenv.load_dotenv()
token = os.getenv('REDLIST_API_TOKEN')


# Test token existence - This is an integrated secret in CI/CD
def test_token_exists():
    assert token is not None, "Missing Red List API token"

def test_factory_from_assessment_id():
    factory = redlistapi.AssessmentFactory(token=token)
    factory.from_assessment_id(assessment_id=181836360)

def test_factory_from_scientific_name():
    factory = redlistapi.AssessmentFactory(token=token)
    factory.from_scientific_name(genus_name='Upupa', species_name='epops')

def test_factory_from_taxid():
    factory = redlistapi.AssessmentFactory(token=token)
    factory.from_taxid(taxid=22682655)
  

if __name__ == "__main__":
    import pytest
    pytest.main([__file__])