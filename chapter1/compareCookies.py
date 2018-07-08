if __name__ == '__main__':
    cookie_a = "BAIDUID=7EE6075F7669DDA4BFADD70458C87E27:FG=1; PSTM=1524022633; BIDUPSID=CCF0DFB0A9EEAEB80C7E0230FD5F4F0E; __cfduid=dec0a5187e20faa4ca6b403625930396b1527167592; MCITY=-%3A; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; PSINO=6; H_PS_PSSID=1455_21096_20718; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; locale=zh; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1531052110; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1531060093; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D"
    cookie_b = "BAIDUID=7EE6075F7669DDA4BFADD70458C87E27:FG=1; PSTM=1524022633; BIDUPSID=CCF0DFB0A9EEAEB80C7E0230FD5F4F0E; __cfduid=dec0a5187e20faa4ca6b403625930396b1527167592; MCITY=-%3A; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; PSINO=6; H_PS_PSSID=1455_21096_20718; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; locale=zh; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1531052110; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1531063285; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D"

    def getCookieMaps(values):
        cookie_maps = {}
        for value in values:
            data = value.strip()
            cookie_maps[data[0:data.index("=")]] = data[data.index("=") + 1:]
        return cookie_maps
        pass


    cookie_a_maps = getCookieMaps(cookie_a.split(";"))
    cookie_b_maps = getCookieMaps(cookie_b.split(";"))

    for key,value in cookie_a_maps.items():
        value_b = cookie_b_maps[key]
        print("key: ", key)
        print("value_a: ", value)
        print("value_b: ", value_b)
        print("----------------------------")

