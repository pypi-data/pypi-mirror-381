import pytest
import numpy as np
from scipy.spatial.transform import Rotation as Rotation
from py3dframe import Frame, FrameTransform

def test_transform_initialization():
    frame_E = Frame.canonical()
    frame_F = Frame.from_axes(origin=[1, 2, 3], x_axis=[1, 0, 0], y_axis=[0, 1, 0], z_axis=[0, 0, 1])
    transform = FrameTransform(input_frame=frame_E, output_frame=frame_F, dynamic=True, convention=0)

    assert transform.input_frame == frame_E
    assert transform.output_frame == frame_F
    assert transform.dynamic is True
    assert transform.convention == 0

def test_rotation_matrix():
    frame_E = Frame.canonical()
    frame_F = Frame.from_axes(origin=[1, 2, 3], x_axis=[1, 0, 0], y_axis=[0, 1, 0], z_axis=[0, 0, 1])
    transform = FrameTransform(input_frame=frame_E, output_frame=frame_F, dynamic=True, convention=0)

    rotation_matrix_expected = np.eye(3)
    rotation_matrix_actual = transform.rotation_matrix

    assert np.allclose(rotation_matrix_actual, rotation_matrix_expected)

def test_translation_vector():
    frame_E = Frame.canonical()
    frame_F = Frame.from_axes(origin=[1, 2, 3], x_axis=[1, 0, 0], y_axis=[0, 1, 0], z_axis=[0, 0, 1])
    transform = FrameTransform(input_frame=frame_E, output_frame=frame_F, dynamic=True, convention=0)

    translation_expected = np.array([[1], [2], [3]])
    translation_actual = transform.translation

    assert np.allclose(translation_actual, translation_expected)

def test_transform_point():
    frame_E = Frame.canonical()
    frame_F = Frame.from_axes(origin=[1, 2, 3], x_axis=[1, 0, 0], y_axis=[0, 1, 0], z_axis=[0, 0, 1])
    transform = FrameTransform(input_frame=frame_E, output_frame=frame_F, dynamic=True, convention=0)

    point_E = np.array([4, 5, 6]).reshape((3, 1))
    point_F = transform.transform(point=point_E)

    expected_point_F = np.array([[3], [3], [3]])
    assert np.allclose(point_F, expected_point_F)

def test_inverse_transform_point():
    frame_E = Frame.canonical()
    frame_F = Frame.from_axes(origin=[1, 2, 3], x_axis=[1, 0, 0], y_axis=[0, 1, 0], z_axis=[0, 0, 1])
    transform = FrameTransform(input_frame=frame_E, output_frame=frame_F, dynamic=True, convention=0)

    point_F = np.array([1, 2, 3]).reshape((3, 1))
    point_E = transform.inverse_transform(point=point_F)

    expected_point_E = np.array([[2], [4], [6]])
    assert np.allclose(point_E, expected_point_E)

def test_transform_vector():
    frame_E = Frame.canonical()
    frame_F = Frame.from_axes(origin=[1, 2, 3], x_axis=[1, 0, 0], y_axis=[0, 1, 0], z_axis=[0, 0, 1])
    transform = FrameTransform(input_frame=frame_E, output_frame=frame_F, dynamic=True, convention=0)

    vector_E = np.array([1, 0, 0]).reshape((3, 1))
    vector_F = transform.transform(vector=vector_E)

    expected_vector_F = np.array([[1], [0], [0]])
    assert np.allclose(vector_F, expected_vector_F)

def test_invalid_convention():
    frame_E = Frame.canonical()
    frame_F = Frame.from_axes(origin=[1, 2, 0], x_axis=[1, 0, 0], y_axis=[0, 1, 0], z_axis=[0, 0, 1])
    with pytest.raises(ValueError):
        FrameTransform(input_frame=frame_E, output_frame=frame_F, dynamic=True, convention=8)

def test_transform_point_dynamique():
    frame_E = Frame.canonical()
    frame_F = Frame.from_axes(origin=[1, 2, 0], x_axis=[1, 0, 0], y_axis=[0, 1, 0], z_axis=[0, 0, 1])
    frame_G = Frame.from_axes(origin=[0, 0, 0], x_axis=[1, -1, 0], y_axis=[1, 1, 0], z_axis=[0, 0, 1], parent=frame_F)
    transform = FrameTransform(input_frame=frame_E, output_frame=frame_G, dynamic=True, convention=0)

    point_E = np.array([4, 5, 6]).reshape((3, 1))
    point_G = transform.transform(point=point_E)

    expected_point_G = np.array([[0], [3 * np.sqrt(2)], [6]])
    assert np.allclose(point_G, expected_point_G)

    # Lets move F
    frame_F.origin = np.array([1, 4, 0])

    point_G = transform.transform(point=point_E)
    expected_point_G = np.array([[np.sqrt(2)], [2 * np.sqrt(2)], [6]])

    # Lets again move F without dynamic
    transform.dynamic = False
    frame_F.origin = np.array([1, 2, 0])

    point_G = transform.transform(point=point_E)
    expected_point_G = np.array([[np.sqrt(2)], [2 * np.sqrt(2)], [6]])
    
    assert np.allclose(point_G, expected_point_G)

    # Lets move F again with dynamic
    transform.dynamic = True

    point_G = transform.transform(point=point_E)
    expected_point_G = np.array([[0], [3 * np.sqrt(2)], [6]])

    assert np.allclose(point_G, expected_point_G)
    

def test_dynamic():
    """
    Test the dynamic behavior of FrameTransform objects.
    """

    # ----------------------------------------------------------------------
    # 1️⃣  Set‑up a canonical (global) frame and a local frame.
    # ----------------------------------------------------------------------
    canonical = Frame.canonical()                     # Global frame (origin at 0,0,0)
    local = Frame.from_axes(                          # Local frame with origin (1,2,3)
        origin=[1, 2, 3],
        x_axis=[1, 0, 0],
        y_axis=[0, 1, 0],
        z_axis=[0, 0, 1],
    )

    # ----------------------------------------------------------------------
    # 1️⃣  Create a *dynamic* transformation and verify it reacts to changes.
    # ----------------------------------------------------------------------
    tf = FrameTransform(
        input_frame=canonical,
        output_frame=local,
        dynamic=True,          # start in dynamic mode
        convention=0,
    )

    # Input point (column vector)
    X_i = np.array([1, 2, 3]).reshape((3, 1))

    # With the canonical frame at the origin the transformed point should be zero.
    X_o = tf.transform(point=X_i)
    np.testing.assert_allclose(X_o, np.zeros((3, 1)), atol=1e-12)

    # Move the input frame – because we are in dynamic mode the result must update.
    canonical.origin = [1, 1, 1]
    X_o = tf.transform(point=X_i)
    np.testing.assert_allclose(
        X_o, np.array([[1.0], [1.0], [1.0]]), atol=1e-12
    )

    # The active input frame reported by the transform must match the modified frame.
    active = tf.get_active_input_frame()
    assert np.allclose(active.origin, [[1.0], [1.0], [1.0]])
    assert np.allclose(active.x_axis, [[1.0], [0.0], [0.0]])
    assert np.allclose(active.y_axis, [[0.0], [1.0], [0.0]])
    assert np.allclose(active.z_axis, [[0.0], [0.0], [1.0]])

    # ----------------------------------------------------------------------
    # 2️⃣  Switch to *static* mode – further changes should no longer affect the result.
    # ----------------------------------------------------------------------
    tf.dynamic = False

    # The last computed result (‑1,‑1,‑1) must stay the same.
    X_o_static = tf.transform(point=X_i)
    np.testing.assert_allclose(
        X_o_static, np.array([[1.0], [1.0], [1.0]]), atol=1e-12
    )

    # Change the canonical frame again – the output must remain unchanged.
    canonical.origin = [2, 2, 2]
    X_o_after = tf.transform(point=X_i)
    np.testing.assert_allclose(
        X_o_after, np.array([[1.0], [1.0], [1.0]]), atol=1e-12
    )

    # Internally the stored input_frame reflects the new origin,
    # but `get_active_input_frame` still returns the old (pre‑change) state.
    assert np.allclose(tf.input_frame.origin, [[2.0], [2.0], [2.0]])
    active_static = tf.get_active_input_frame()
    assert np.allclose(active_static.origin, [[1.0], [1.0], [1.0]])

    # ----------------------------------------------------------------------
    # 3️⃣  Replace the input frame with a completely new one,
    #     then re‑enable dynamic mode and verify the transform updates.
    # ----------------------------------------------------------------------
    new_input = Frame.from_axes(
        origin=[3, 3, 3],
        x_axis=[0, 1, 0],
        y_axis=[0, 0, 1],
        z_axis=[1, 0, 0],  
    )
    tf.input_frame = new_input

    # While still static, the transformation should still use the *old* frame.
    active_static = tf.get_active_input_frame()
    assert np.allclose(active_static.origin, [[1.0], [1.0], [1.0]])


    # Reactivate dynamic mode – now the new input frame is taken into account.
    tf.dynamic = True

    # `get_active_input_frame` must now report the newly assigned frame.
    active_new = tf.get_active_input_frame()
    assert np.allclose(active_new.origin, [[3.0], [3.0], [3.0]])
    assert np.allclose(active_new.x_axis, [[0.0], [1.0], [0.0]])
    assert np.allclose(active_new.y_axis, [[0.0], [0.0], [1.0]])
    assert np.allclose(active_new.z_axis, [[1.0], [0.0], [0.0]])