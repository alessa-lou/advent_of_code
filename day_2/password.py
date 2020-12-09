class Password():

    def convert_input_to_dict(self):
        policy_dict = {}
        policy_list = []
        f = open("input.txt")
        file_content = [line.rstrip() for line in f.readlines()]
        for line in file_content:
            pp_list = line.split()
            # print("printing pp_list", pp_list)
            min_max = pp_list[0].split("-")
            policy_dict["min"] = int(min_max[0])
            policy_dict["max"] = int(min_max[1])
            policy_dict["char"] = pp_list[1][0]
            policy_dict["password"] = pp_list[2]
            # print("printing pol dict", policy_dict)
            policy_list.append(policy_dict)
            print("printing pol list method 1", policy_list)
            return policy_list
        
    
    def meets_policy(self):
        policy_list = self.convert_input_to_dict()
        print("printing pol list", policy_list)
        for dictionary in policy_list:
            char_count = dictionary["password"].count(dictionary["char"])
            print("printing char count", char_count)

