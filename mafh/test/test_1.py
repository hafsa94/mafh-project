class TestX(object):

    _SEARCH_PARAM = {"desc": {"description": "python"},
                     "loc": {"location": "new york"},
                     "type": {"full_time": "true"},
                     "desc_loc": {"description": "software engineer", "location": "vienna"},
                     "desc_type": {"description": "java", "full_time": "true"},
                     "type_loc": {"location": "berlin", "full_time": "true"},
                     "desc_loc_type": {"location": "japan", "description": "python", "full_time": "true"},
                     }

    def test_01_search_by_description_results(self, setup):
        """Test search by description results"""
        params = self._SEARCH_PARAM["desc"]
        req = setup.get_request(params)
        # Checks the status code if it is 200 or not
        assert setup.verify_request_response(req)
        req_data = setup.get_request_data(req)
        # Checks all the search terms present in the response or not
        assert setup.verify_search_result(req_data, params)

    def test_02_search_by_location_results(self, setup):
        """Test search by location results"""
        params = self._SEARCH_PARAM["loc"]
        req = setup.get_request(params)
        # Checks the status code if it is 200 or not
        assert setup.verify_request_response(req)
        req_data = setup.get_request_data(req)
        # Checks all the search terms present in the response or not
        assert setup.verify_search_result(req_data, params)

    def test_03_search_by_type_results(self, setup):
        """Test search by type results"""
        params = self._SEARCH_PARAM["type"]
        req = setup.get_request(params)
        # Checks the status code if it is 200 or not
        assert setup.verify_request_response(req)
        req_data = setup.get_request_data(req)
        # Checks all the search terms present in the response or not
        assert setup.verify_search_result(req_data, params)

    def test_04_search_by_description_n_location_results(self, setup):
        """Test search by description and location results"""
        params = self._SEARCH_PARAM["desc_loc"]
        req = setup.get_request(params)
        # Checks the status code if it is 200 or not
        assert setup.verify_request_response(req)
        req_data = setup.get_request_data(req)
        # Checks all the search terms present in the response or not
        assert setup.verify_search_result(req_data, params)

    def test_05_search_by_description_n_type_results(self, setup):
        """Test search by description and type results"""
        params = self._SEARCH_PARAM["desc_type"]
        req = setup.get_request(params)
        # Checks the status code if it is 200 or not
        assert setup.verify_request_response(req)
        req_data = setup.get_request_data(req)
        # Checks all the search terms present in the response or not
        assert setup.verify_search_result(req_data, params)

    def test_06_search_by_location_n_type_results(self, setup):
        """Test search by location and type results"""
        params = self._SEARCH_PARAM["type_loc"]
        req = setup.get_request(params)
        # Checks the status code if it is 200 or not
        assert setup.verify_request_response(req)
        req_data = setup.get_request_data(req)
        # Checks all the search terms present in the response or not
        assert setup.verify_search_result(req_data, params)

    def test_07_search_by_description_location_n_type_results(self, setup):
        """Test search by description, location and type results"""
        params = self._SEARCH_PARAM["desc_loc_type"]
        req = setup.get_request(params)
        # Checks the status code if it is 200 or not
        assert setup.verify_request_response(req)
        req_data = setup.get_request_data(req)
        # Checks all the search terms present in the response or not
        assert setup.verify_search_result(req_data, params)

    def test_08_jobs_count_50_per_page(self, setup):
        """Verify jobs count per page is less than or equal to 50"""
        params = self._SEARCH_PARAM["type"]
        req = setup.get_request(params)
        # Checks the status code if it is 200 or not
        assert setup.verify_request_response(req)
        req_data = setup.get_request_data(req)
        print(len(req_data))
        # Checks the count of jobs per page is <= 50
        assert setup.verify_pagination_result(req_data)

    def test_09_verify_pagination(self, setup):
        """Test pagination
        NOTE: API response don't have any information regarding the total number of jobs
                hence can not loop on next pages"""
        params = self._SEARCH_PARAM["type"]
        req = setup.get_request(params, page=1)
        # Checks the status code if it is 200 or not
        assert setup.verify_request_response(req)
        req_data = setup.get_request_data(req)
        print(len(req_data))
        # Checks the count of jobs in the current page is <= 50
        assert setup.verify_pagination_result(req_data)




