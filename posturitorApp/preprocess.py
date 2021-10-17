import cv2
import mediapipe as mp
import os
import numpy as np

ref_path = 'yujing_MBA_1/ref.jpg'

def extractArray(cand_path):
    mp_pose = mp.solutions.pose
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        file = cand_path
        frame = cv2.imread(file)
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = pose.process(image)

        m = []
        for l in results.pose_landmarks.landmark[:13]:
            m.append([l.x, l.y, l.z, l.visibility])
        
        m_array = np.array(m)

#         save_path = cand_path + '_array.npy'
#         np.save(save_path, m_array)
    return m_array

def extractFeature(cand_path, ref_path):
    cand_array = extractArray(cand_path)
    ref_array = extractArray(ref_path)

    diff = cand_array - ref_array

    a1 = np.array([cand_array[1] - cand_array[4]])
    a2 = np.array([cand_array[2] - cand_array[5]])
    a3 = np.array([cand_array[3] - cand_array[6]])
    a4 = np.array([cand_array[7] - cand_array[8]])
    a5 = np.array([cand_array[9] - cand_array[10]])
    a6 = np.array([cand_array[11] - cand_array[12]])


    feature = np.concatenate([cand_array,a1,a2,a3,a4,a5,a6, diff])
    feature = feature.flatten()
#     save_path = cand_path + '_feature.npy'
#     np.save(save_path, feature)

    return feature


if __name__ == "__main__":
    cand_path = 'yujing_MBA_1/B_D/19.jpeg'
    print(extractFeature(cand_path, ref_path))