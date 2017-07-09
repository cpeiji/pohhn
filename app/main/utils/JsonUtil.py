class JsonUtil:

    @staticmethod
    def list_obj_dict(list):
        new_list = []
        for obj in list:
            new_list.append(obj.__dict__)
        return new_list


