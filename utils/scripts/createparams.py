
ITERATIONS      = [5]
INTENSITY       = [4.0]  # [2.0, 4.0, 8.0]  # [0.0, 0.5, 1.0]
THRESHOLD       = [0.0, 0.8, 10.0]
SOFT_THRESHOLD  = [0.0, 0.5, 1.0]
ANTI_FLICKER    = [
    # True,   # 13-tap + 9-tap
    False,  # dual-filtering
]


if __name__ == "__main__":

    bloom_params = {
        "iterations": 5,
        "intensity": 0.5,
        "threshold": 0.8,
        "soft_threshold": 0.5,
        "anti_flicker": False,
        # "debug_blur": False,
    }

    n_of_test_scenes = 0

    for iterations in ITERATIONS:
        bloom_params["iterations"] = iterations
        for intensity in INTENSITY:
            bloom_params["intensity"] = intensity
            for threshold in THRESHOLD:
                bloom_params["threshold"] = threshold
                for soft_threshold in SOFT_THRESHOLD:
                    bloom_params["soft_threshold"] = soft_threshold
                    for anti_flicker in ANTI_FLICKER:
                        bloom_params["anti_flicker"] = anti_flicker
                        n_of_test_scenes += 1
                        print(bloom_params)  # TODO capture and forward to setparams.py

    print(f"{n_of_test_scenes=}")

    new_stage_params = { "bloom_stage": bloom_params }
