import requests


class UtilityFunctions(object):

    @staticmethod
    def short_location(text):
        """
        Created short form for the given text example: returns "NY" for "New York"
        :param text: String for which short form is needed
        :return: String of short form
        """
        return "".join([t[0] for t in text.split()]).lower()

    @staticmethod
    def get_request(search_param, page=0):
        """
        Creates a GET request for the given api and params
        :param search_param: Dictionary of search parameter as a key and its value example: {"description": "python"}
        :param page: Integer to specify page number of the results. By default it is 0
        :return: Response object
        """
        search_string = ""
        for key, value in search_param.items():
            search_string = search_string + key + "=" + value + "&"
        if page > 0:
            search_string = search_string + "page=" + str(page) + "&"
        print("https://jobs.github.com/positions.json?" + search_string[:-1])
        res = requests.get("https://jobs.github.com/positions.json?" + search_string[:-1])
        return res

    @staticmethod
    def verify_request_response(res):
        """
        Verifies if the status code is 200 or not
        :param res: Response object
        :return: Boolean True or False
        """
        return res.status_code == 200

    @staticmethod
    def get_request_data(res):
        """
        Returns response data
        :param res: Response object
        :return: Response JSON
        """
        return res.json()

    def verify_search_result(self, res_data, search_param):
        """
        Check if the search param value is present in the corresponding response
        example: for param {"description": "python"}, it will search "python" in the value of "description" key
        of response json
        :param res_data: Response JSON
        :param search_param: Dictionary of search parameter as a key and its value example: {"description": "python"}
        :return: Boolean True or False
        """
        result = True
        for data in res_data:
            for key, value in search_param.items():
                if key == "location":
                    result = result and (
                            (value.lower() in data[key].lower()) or
                            (self.short_location(value) in data[key]. lower())
                    )
                elif key == "full_time":
                    result = result and ("Full Time" == data["type"])
                else:
                    result = result and (value.lower() in data[key].lower())
        return result

    @staticmethod
    def verify_pagination_result(res_data):
        """
        Check if jobs count is <= 50
        :param res_data: Response JSON
        :return:  Boolean True or False
        """
        return len(res_data) <= 50
