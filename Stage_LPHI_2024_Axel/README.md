# Stage_LPHI_2024

Done by [Axel de Montgolfier](https://github.com/Axeldmont/) during hi time at the LPHI laboratory in Montpellier University.

---

First of all, all the videos and frames we used for analysis and segmentation were made using a spinning disk confocal microscope that lightens in red the macrophages and in green the calcium flashes. We cut the caudal fin fold of a zebrafish in order to study if there is a connection between the polarization of macrophages and calcium flashes.

The aim of this project is then to segment the macrophages accurately. This segmentation will allow us to layer it on the green channel video to naalyse the calcium flashes of the macrophages we tracked.

## Installation

---

As my internship was the following of his work, I had to ba acostumed to what he has done during his time at LPHI. This folder consists of upgrades of the original work available via this [link](https://github.com/Axeldmont/Stage-LPHI-2024). It also contains the `Set_up` folder that helps you build the project and your dataset.

First of all, the packages you will need in order to run this project are available in the `requirements.txt` file. For the `numena` library, you must add this class in the  `/home/gbouland/micromamba/envs/sam-env/lib/python3.12/site-packages/numena/io/json.py` file. If you didn't set up an environment, find where your `site-packages` folder is stocked and then add the class to the file mentionned before.

```python
class Serializable(ABC):
    """Python Interface to export Python objects to JSON format.

    The child class must implement 'dumps' property.
    """

    @abstractmethod
    def dumps(self) -> dict:
        """Property to generate the JSON formatted data of the current instance."""
        pass
```

Next, as Axel mentionned it, you must add an `input` folder that should look like this :

```
input/yourdatafolder/
  ├── dataset
  ├── models
  ├── results
  ├── vert
      ├── frames #(empty)
      └── greenchannelvideo.mp4
  └── redchannelvideo.mp4
```

Now let's talk about what's inside of these folders. You can refer yourself to the `example` folder.

---

The `dataset` folder is arranged as folloxs :

```
dataset
├── test
    ├── test_x
    └── test_y
├── train
    ├── train_x
    └── train_y
├── dataset.csv
└── META.json
```

The `train` folder consists of `train_x` which is a folder containing all the frames that served to train the model. They must be from the red channel (so macrophages). The `train_y` folder contains the "masks". Each frame in the `train_x` folder must be hand-cut in the ImageJ program. You must add "Regions of Interest" on each frame and then save it as a `.zip` file containing all the ROIs in a single frame. You must do it for all frames in the `train_x` folder. Thanks to `kartezio` and the methods it is using, you don't need a lot of frame to make a good `train` dataset. For instance, Axel used only 26 frames.

Then comes the `test` folder. You don't have to worry about the `test_x` folder as it will be added when you run the final file. It contains the frames of your red channel video. The `test_y` is a bit particular. As for the `train_x` folder, it contains masks. If your video has more frames than your training set, the `test_y` contains all the masks from `train_y` ans the last one is repeated to reach the number of frmaes in your video. All of this is achieved using the `copy_zip_file` function in the `Set_up/Structure.py` file.

The `dataset.csv` file is a summary of the different paths of your dataset. It is possible to make it by running the `Dataset_csv.py` file. Finally, the `META.json` file is linked to the `dataset.csv` file as you can see input and label. Input is an image with format hsv and label are ROI files with format polygon (this `META.json` file was made to match functions from the kartezio library).

---

The `models` folder consists of json files that characterize the model obtained from the train_model.py file in the `Set_up` folder. To set-up your model, I advice you to do it first and to add a few frames in the `test` folder (before you start segmenting your videos, you may delete them later on place them in a different folder).

---

The `results` folder contains the performance of the model in the `results.csv` file that is obtained by the `eval_models.py` file after initializing your model.

---

The `vert` folder contains a `frames` folder that is at first empty. You must place your green channel video in the `vert` folder. By running the `Extract_frames.py` file in the `Set_up` folder (by correctly replacing the path of your green channel video), the `frames` folder will be filled with the frames of your green channel video. Be careful to change the width and height parameters with the dimensions of your videos. It is recommended to use even squared dimensions (1024x1024 for instance).

Finally, you must put you red channel video in the `input/yourdatafolder/` folder.

---

You can execute the `Convert.py` file in the `Set_up` folder to convert AVI files into MP4 as AVI is the preferred format for video extraction from ImageJ (as Python doesn't work well with 16-bit file formats such as TIFF, while MP4, an 8-bit format, is more compatible).

---

The `Example` folder contains a full, ready to use, example dataset that you can use to execute Axel's **Mactrack**.

We advice you to replace the `gettingstarted.py` available in the former Mactrack module by the one you can find in the root.
