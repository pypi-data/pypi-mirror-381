"""
Tests for JSON-based Catastro API endpoints.
"""
import pytest
from unittest.mock import Mock, patch
from pycatastro.client import CatastroClient
from pycatastro.http_client import CatastroApiError
from pycatastro import tipos


class TestCatastroClient:
    """Test the main CatastroClient with mocked responses."""
    
    def setup_method(self):
        self.client = CatastroClient()
    
    @patch('pycatastro.endpoints.callejero.CatastroHttpClient')
    def test_obtener_provincias(self, mock_http_client):
        """Test getting list of provinces."""
        mock_response = {
            "consulta_provincieroResult": {
                "control": {"cuprov": 52, "cuerr": 0},
                "provinciero": {
                    "prov": [
                        {"cpine": "01", "np": "ALAVA"},
                        {"cpine": "02", "np": "ALBACETE"}
                    ]
                }
            }
        }
        mock_http_client.return_value.get_json.return_value = mock_response
        
        result = self.client.obtener_provincias()
        
        assert result == mock_response
        mock_http_client.return_value.get_json.assert_called_once_with(
            "OVCServWeb/OVCWcfCallejero/COVCCallejero.svc/json/ObtenerProvincias"
        )
    
    @patch('pycatastro.endpoints.callejero.CatastroHttpClient')
    def test_obtener_municipios(self, mock_http_client):
        """Test getting list of municipalities."""
        mock_response = {
            "consulta_municipieroResult": {
                "control": {"cumun": 1, "cuerr": 0},
                "municipiero": {
                    "muni": [
                        {
                            "locat": {"cd": "46", "cmc": "900"},
                            "loine": {"cp": "46", "cm": "250"},
                            "nm": "VALENCIA"
                        }
                    ]
                }
            }
        }
        mock_http_client.return_value.get_json.return_value = mock_response
        
        result = self.client.obtener_municipios("VALENCIA")
        
        assert result == mock_response
        mock_http_client.return_value.get_json.assert_called_once_with(
            "OVCServWeb/OVCWcfCallejero/COVCCallejero.svc/json/ObtenerMunicipios",
            {"Provincia": "VALENCIA", "Municipio": ""}
        )
    
    @patch('pycatastro.endpoints.callejero.CatastroHttpClient')
    def test_obtener_callejero(self, mock_http_client):
        """Test getting list of streets."""
        mock_response = {
            "consulta_callejeroResult": {
                "control": {"cuca": 1, "cuerr": 0},
                "callejero": {
                    "calle": [
                        {
                            "loine": {"cp": "46", "cm": "250"},
                            "dir": {"cv": "00101", "tv": "CL", "nv": "MAYOR"}
                        }
                    ]
                }
            }
        }
        mock_http_client.return_value.get_json.return_value = mock_response
        
        result = self.client.obtener_callejero("VALENCIA", "VALENCIA", tipos.CALLE, "MAYOR")
        
        assert result == mock_response
        mock_http_client.return_value.get_json.assert_called_once_with(
            "OVCServWeb/OVCWcfCallejero/COVCCallejero.svc/json/ObtenerCallejero",
            {"Provincia": "VALENCIA", "Municipio": "VALENCIA", "TipoVia": "CL", "NomVia": "MAYOR"}
        )
    
    @patch('pycatastro.endpoints.callejero.CatastroHttpClient')
    def test_consulta_dnploc(self, mock_http_client):
        """Test querying cadastral data by location."""
        mock_response = {
            "consulta_dnplocResult": {
                "control": {"cunum": 1, "cuerr": 0},
                "numerero": {
                    "nump": [
                        {
                            "pc": {"pc1": "4630701XJ", "pc2": "1741S0001UR"},
                            "num": {"pnp": "1"}
                        }
                    ]
                }
            }
        }
        mock_http_client.return_value.get_json.return_value = mock_response
        
        result = self.client.consulta_dnploc("VALENCIA", "VALENCIA", calle="MAYOR", numero="1")
        
        assert result == mock_response
    
    @patch('pycatastro.endpoints.coordenadas.CatastroHttpClient')
    def test_consulta_rccoor(self, mock_http_client):
        """Test querying cadastral reference by coordinates."""
        mock_response = {
            "Consulta_RCCOORResult": {
                "control": {"cucoor": 1, "cuerr": 0},
                "coordenadas": {
                    "coord": [
                        {
                            "pc": {"pc1": "4630701XJ", "pc2": "1741S0001UR"},
                            "geo": {"xcen": "728015.00", "ycen": "4372193.00", "srs": "EPSG:25830"},
                            "ldt": "2023-01-01T00:00:00"
                        }
                    ]
                }
            }
        }
        mock_http_client.return_value.get_json.return_value = mock_response
        
        result = self.client.consulta_rccoor("728015.00", "4372193.00", "EPSG:25830")
        
        assert result == mock_response
        mock_http_client.return_value.get_json.assert_called_once_with(
            "OVCServWeb/OVCWcfCallejero/COVCCoordenadas.svc/json/Consulta_RCCOOR",
            {"CoorX": "728015.00", "CoorY": "4372193.00", "SRS": "EPSG:25830"}
        )


class TestTipos:
    """Test the tipos constants."""
    
    def test_street_types_exist(self):
        """Test that common street types are defined."""
        assert tipos.CALLE == "CL"
        assert tipos.AVENIDA == "AV"
        assert tipos.PLAZA == "PZ"
        assert tipos.PASEO == "PS"
        assert tipos.CARRETERA == "CR"
    
    def test_all_types_are_strings(self):
        """Test that all tipo constants are strings."""
        for attr_name in dir(tipos):
            if not attr_name.startswith('_'):
                attr_value = getattr(tipos, attr_name)
                assert isinstance(attr_value, str)
                assert len(attr_value) <= 3  # All codes are 2-3 characters


class TestErrorHandling:
    """Test error handling in HTTP client."""
    
    @patch('pycatastro.http_client.requests.Session')
    def test_api_error_raised(self, mock_session):
        """Test that API errors are properly raised."""
        from pycatastro.http_client import CatastroHttpClient
        
        # Mock response with API error
        mock_response = Mock()
        mock_response.json.return_value = {
            "consulta_provincieroResult": {
                "control": {"cuerr": 1},
                "lerr": [{"cod": "001", "des": "Test error message"}]
            }
        }
        mock_response.raise_for_status.return_value = None
        mock_session.return_value.get.return_value = mock_response
        
        client = CatastroHttpClient()
        
        with pytest.raises(CatastroApiError) as exc_info:
            client.get_json("test/endpoint")
        
        assert "Test error message" in str(exc_info.value)


@pytest.mark.integration
class TestIntegrationWithRealAPI:
    """
    Integration tests that make real API calls.
    These are marked as integration tests and may be skipped in CI.
    """
    
    def setup_method(self):
        self.client = CatastroClient()
    
    @pytest.mark.skip(reason="Requires internet connection")
    def test_real_obtener_provincias(self):
        """Test real API call to get provinces."""
        result = self.client.obtener_provincias()
        
        # Basic structure validation
        assert "consulta_provincieroResult" in result
        assert "control" in result["consulta_provincieroResult"]
        assert "provinciero" in result["consulta_provincieroResult"]
        
        # Should have provinces
        provincias = result["consulta_provincieroResult"]["provinciero"]["prov"]
        assert len(provincias) > 0
        
        # Each province should have code and name
        for prov in provincias:
            assert "cpine" in prov
            assert "np" in prov
    
    @pytest.mark.skip(reason="Requires internet connection")
    def test_real_obtener_municipios_valencia(self):
        """Test real API call to get municipalities for Valencia."""
        result = self.client.obtener_municipios("VALENCIA")
        
        # Basic structure validation
        assert "consulta_municipieroResult" in result
        assert "control" in result["consulta_municipieroResult"]
        
        # Should not error
        assert result["consulta_municipieroResult"]["control"]["cuerr"] == 0