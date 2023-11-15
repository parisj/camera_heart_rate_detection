import plotly.express as px
import plotly.graph_objects as go
from scipy import signal
import numpy as np


def plot_frame(frame_data):
    """
    Plot frame data as an image.
    """
    return px.imshow(frame_data, binary_string=True)


def plot_roi(roi_data):
    """
    Plot ROI (Region of Interest) data as an image.
    """
    return px.imshow(roi_data, binary_string=True)


def plot_rgb_channels(rgb_data):
    """
    Plot RGB channels.
    """
    return {
        "data": [
            {
                "x": list(range(256)),
                "y": list(rgb_data[0]),
                "type": "scatter",
                "name": "R",
                "marker": {"color": "red"},
            },
            {
                "x": list(range(256)),
                "y": list(rgb_data[1]),
                "type": "scatter",
                "name": "G",
                "marker": {"color": "green"},
            },
            {
                "x": list(range(256)),
                "y": list(rgb_data[2]),
                "type": "scatter",
                "name": "B",
                "marker": {"color": "blue"},
            },
        ],
        "layout": {"title": "RGB Channels"},
    }


def plot_head_pose(head_pose):
    """
    Plot Head Pose Angles.
    """
    return {
        "data": [
            {
                "x": list(range(256)),
                "y": list(head_pose[0]),
                "type": "scatter",
                "name": "pitch (x)",
            },
            {
                "x": list(range(256)),
                "y": list(head_pose[1]),
                "type": "scatter",
                "name": "yaw (y)",
            },
            {
                "x": list(range(256)),
                "y": list(head_pose[2]),
                "type": "scatter",
                "name": "roll (z)",
            },
        ],
        "layout": {"title": "3D Head Pose angles"},
    }


def plot_rPPG_signal_and_noise(rPPG, rPPG_filtered, rhythmic):
    """
    Plot rPPG signal.
    """
    return {
        "data": [
            {
                "x": list(range(256)),
                "y": list(rPPG),
                "type": "scatter",
                "name": "rPPG",
            },
            {
                "x": list(range(256)),
                "y": list(rPPG_filtered),
                "type": "scatter",
                "name": "Processed rPPG",
            },
            {
                "x": list(range(256)),
                "y": list(rhythmic),
                "type": "scatter",
                "name": "rhythmic subtracted (no filtering)",
            },
        ],
        "layout": {"title": "rPPG signal"},
    }


def plot_frequency_domain(sig, fs=30):
    """
    Plot the frequency domain representation of the signal.

    """
    # Compute the Fourier Transform of the signal
    sig_fft = np.fft.fft(sig)

    # Compute the two-sided spectrum
    two_sided_spectrum = np.abs(sig_fft) / len(sig)

    # Compute the one-sided spectrum (only positive frequencies)
    one_sided_spectrum = two_sided_spectrum[: len(sig) // 2]

    # Create frequency axis (only positive frequencies)
    freq_axis = np.fft.fftfreq(len(sig), 1 / fs)[: len(sig) // 2]

    # Create Plotly figure
    fig = go.Figure()

    # Add trace for spectrum
    fig.add_trace(
        go.Scatter(x=freq_axis, y=one_sided_spectrum, mode="lines", name="Magnitude")
    )

    # Update layout
    fig.update_layout(
        title="Frequency domain representation",
        xaxis_title="Frequency [Hz]",
        yaxis_title="Magnitude",
        template="plotly_white",
    )

    return fig


def plot_post_processed_rPPG(rppg_signal):
    """
    Plot the post-processed rPPG signal.

    """
    # Create a sequence of indices for the x-axis based on the length of the rPPG signal
    time_axis = np.arange(len(rppg_signal))

    # Create Plotly figure
    fig = go.Figure()

    # Add trace for the rPPG signal
    fig.add_trace(
        go.Scatter(x=time_axis, y=rppg_signal, mode="lines", name="rPPG Signal")
    )

    # Update layout
    fig.update_layout(
        title="Post-Processed rPPG Signal",
        xaxis_title="Sample Number",
        yaxis_title="Amplitude",
        template="plotly_white",
    )

    return fig


def plot_hr(hr, hr_old):
    hr = hr * 60
    hr_old = hr_old * 60
    fig = go.Figure()
    fig.add_trace(
        go.Indicator(
            mode="number+delta",
            value=hr,
            domain={"x": [0, 0.5], "y": [0.5, 1]},
            delta={"reference": hr_old, "relative": False},
            title={"text": "Heart Rate", "font": {"size": 24}},
        )
    )
    return fig
