import json

class Setting():
    freq_start = None
    freq_end = None
    freq_step = None
    sample_size = None
    power_threshold = None

    @staticmethod
    def load_setting(file:str):
        with open(file) as f:
            config = json.load(f)
            Setting.freq_start = int(float(config["freq_start"])*1e6) # MHz
            Setting.freq_end = int(float(config["freq_end"])*1e6) #GHz
            Setting.freq_step = int(float(config["freq_step"])*1e3) # KHz
            Setting.sample_size = int(config["sample_size"]) 
            Setting.sample_rate = int(float(config["sample_rate"])*1e6) # MHz
            Setting.power_threshold = float(config["power_threshold"]) # 55.0


if __name__ == "__main__":
    Setting.load_setting("/home/alan/workspace-python/RTL-SDR/rf-surveillance-node/src/setting.json")
    print(Setting.freq_start)
    print(Setting.freq_end)
    print(Setting.freq_step)
    print(Setting.sample_size)
    print(Setting.sample_rate)
    print(Setting.power_threshold)


   