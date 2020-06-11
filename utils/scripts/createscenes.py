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

    for iterations in [5]:
        bloom_params["iterations"] = iterations
        for intensity in [2.0, 4.0, 8.0]:  # [0.0, 0.5, 1.0]
            bloom_params["intensity"] = intensity
            for threshold in [0.0, 0.8, 10.0]:
                bloom_params["threshold"] = threshold
                for soft_threshold in [0.0, 0.5, 1.0]:
                    bloom_params["soft_threshold"] = soft_threshold
                    for anti_flicker in [True, False]:
                        bloom_params["anti_flicker"] = anti_flicker
                        n_of_test_scenes += 1
                        print(bloom_params)  # TODO capture and forward to setparams.py

    print(f"{n_of_test_scenes=}")

    new_stage_params = { "bloom_stage": bloom_params }
