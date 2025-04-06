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
            Setting.freq_start = int(float(config["freq_start"])*1e6) # from MHz to Hz
            Setting.freq_end = int(float(config["freq_end"])*1e6) # from MHz to Hz
            Setting.freq_step = int(float(config["freq_step"])*1e3) # from KHz to Hz
            Setting.sample_size = int(config["sample_size"]) 
            Setting.sample_rate = int(float(config["sample_rate"])*1e6) # from MHz to Hz
            Setting.power_threshold = float(config["power_threshold"]) # 56.0 dbm


if __name__ == "__main__":
    Setting.load_setting("/home/alan/workspace-python/RTL-SDR/rf-surveillance-node/src/setting.json")
    print(Setting.freq_start)
    print(Setting.freq_end)
    print(Setting.freq_step)
    print(Setting.sample_size)
    print(Setting.sample_rate)
    print(Setting.power_threshold)


   