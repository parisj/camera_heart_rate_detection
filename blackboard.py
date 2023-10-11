from collections import deque
from typing import List, Tuple
import numpy as np


class Blackboard:
    def __init__(self, max_len: int) -> None:
        self.frame = None
        self.roi = None
        self.max_len = max_len
        self.samples_r = deque(maxlen=max_len)
        self.samples_b = deque(maxlen=max_len)
        self.samples_g = deque(maxlen=max_len)

        self.samples_head_x = deque(maxlen=max_len)
        self.samples_head_y = deque(maxlen=max_len)
        self.samples_head_z = deque(maxlen=max_len)
        self.samples_rPPG = None
        self.samples_rhythmic = None
        self.bandpass_filtered = None
        self.signal_processor = None

    def update_frame(self, frame: np.array) -> None:
        self.frame = frame

    def update_roi(self, roi: np.array) -> None:
        self.roi = roi

    def update_samples_rgb(self, sample_rgb) -> None:
        self.samples_r.append(sample_rgb[2])
        self.samples_g.append(sample_rgb[1])
        self.samples_b.append(sample_rgb[0])

    def update_samples_head_pose(self, head_pose: np.array) -> None:
        self.samples_head_x.append(head_pose[0])
        self.samples_head_y.append(head_pose[1])
        self.samples_head_z.append(head_pose[2])

    def update_samples_rPPG(self, rPPG: np.array) -> None:
        self.samples_rPPG = rPPG

    def update_samples_rhythmic(self, rhythmic: np.array) -> None:
        self.samples_rhythmic = rhythmic

    def update_bandpass_filtered(self, bandpass_filtered: np.array) -> None:
        self.bandpass_filtered = bandpass_filtered

    def get_frame(self) -> np.array:
        return self.frame

    def get_roi(self) -> np.array:
        return self.roi

    def get_samples_rgb(self) -> deque:
        return self.samples_r, self.samples_g, self.samples_b

    def get_samples_head_pose(self) -> deque:
        return self.samples_head_x, self.samples_head_y, self.samples_head_z

    def get_samples_rPPG(self) -> deque:
        return self.samples_rPPG

    def get_samples_rhythmic(self) -> deque:
        return self.samples_rhythmic

    # TODO Expand this method to return all samples
    def get_samples(self) -> Tuple:
        # print("Getting samples \n")
        # print(
        #    "Samples RGB: \n",
        #    self.samples_r,
        #    "\n",
        #    self.samples_g,
        #    "\n",
        #    self.samples_b,
        #    "\n",
        # )
        # print(
        #    "Samples Head Pose: \n",
        #    self.samples_head_x,
        #    "\n",
        #    self.samples_head_y,
        #    "\n",
        #    self.samples_head_z,
        #    "\n",
        # )
        samples_rgb = self.get_samples_rgb()
        samples_head_pose = self.get_samples_head_pose()
        return self.frame, self.roi, samples_rgb, samples_head_pose

    def get_samples_signals(self) -> Tuple:
        samples_rgb = self.get_samples_rgb()
        samples_head_pose = self.get_samples_head_pose()
        return samples_rgb, samples_head_pose

    def get_bandpass_filtered(self) -> np.array:
        return self.bandpass_filtered
