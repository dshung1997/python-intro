import json
import time
import copy

modify_data = {
    "expiration_time": 200,
    "product": "qchat",
    "utm_campaign": str(time.time()),
    "storefront": {
        "banner_enabled": False,
        "purchase_options": [
            {
                "button_text": "Dynamic offer 1 - button_text",
                "description": "Dynamic offer 1 - description",
                "id": "",
                "price": "99.99",
                "price_text": "price_text",
                "session_count": "0",
                "subtitle": "Dynamic offer - subtitle",
                "title": "Dynamic offer - title",
                "suffix": "Dynamic offer - suffix",
                "trial_duration": 0,
                "min_member_count": 1,
                "max_member_count": 1,
                "action": "purchase",
                "frequency_view": "monthly",
                "free_learning_subscription": False,
                "team_type": "personal",
                "frequency": None,
            }
        ]
    }
}


class StorefrontConfig:
    def __init__(self, data):
        self.__data = copy.deepcopy(data)

    @property
    def data(self):
        return self.__data

    def update(self, modify_data):
        # modify_data must be a dict

        def recursive(parent_data, selector, new_data):
            if type(parent_data) == list:
                if selector >= len(parent_data):
                    parent_data.extend([(type(new_data))()]
                                       * (len(parent_data) - selector + 1))

            if type(parent_data) == dict:
                if selector not in parent_data:
                    parent_data[selector] = (type(new_data))()

            # --

            if type(new_data) == list:
                for i in range(len(new_data)):
                    recursive(parent_data[selector], i, new_data[i])

            elif type(new_data) == dict:
                for k in new_data:
                    recursive(parent_data[selector], k, new_data[k])

            else:
                parent_data[selector] = new_data

        for k in modify_data:
            recursive(self.__data, k, modify_data[k])

    def __str__(self):
        return json.dumps(self.__data)


class FileController:
    def read_file(self, file_name):
        with open(file_name, "r") as json_file:
            s = json.load(json_file)
            return s

    def write_file(self, config, file_name):
        with open(file_name, "w") as writer:
            writer.write(str(config))


loaded_json = FileController().read_file("data.json")
config = StorefrontConfig(loaded_json)
config.update(modify_data)
FileController().write_file(config, "result.json")
