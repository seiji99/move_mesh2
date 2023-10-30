import pickle
import trimesh
import numpy as np
import random

# データセットを読み込む
with open("../chair_dataset3.pkl", "rb") as pickle_file:
    chair_dataset = pickle.load(pickle_file)

shape_id, style_id, shape_label, scene = chair_dataset[0]

# 移動させたいメッシュの名前リスト
mesh_names_to_move = ["Mesh.006", "Mesh.007", "Mesh.008", "Mesh.001", "Mesh"]

# 移動ベクトル
translation_vector = [random.randint(-20, 20), random.randint(-20, 20), random.randint(-20, 20)]

camera_positions = {"position": [0, 1, 1.5], "target_direction": [0, -0.5, -1], "output_filename": "scene0.png"}

camera_position = camera_positions["position"]

# カメラの向きを調整するための情報
initial_camera_direction = [0, 0, -1]  # カメラの初期向き
target_camera_direction = camera_positions["target_direction"]  # カメラの目標向き

# カメラの初期向きと目標向きから回転行列を計算
rotation_matrix = trimesh.transformations.rotation_matrix(
    trimesh.transformations.angle_between_vectors(initial_camera_direction, target_camera_direction),
    np.cross(initial_camera_direction, target_camera_direction)
)
camera_transform = trimesh.scene.cameras.look_at(
    points=[camera_position],     # カメラの位置を注視点とする
    fov=(60.0, 60.0),             # カメラの視野角を指定
    distance=None,                # カメラの距離を変更しない
    rotation=rotation_matrix,     # 回転を変更
    center=camera_position        # カメラの位置を中心にする
)

scene.camera_transform = camera_transform

# メッシュのループ
# min_y = float("inf")  # 最小のy座標を無限大で初期化
# for name, mesh in scene.geometry.items():
#     if name in mesh_names_to_move:
#         mesh.apply_translation(translation_vector)
#     # メッシュの頂点の中で最小のy座標を更新
#     min_y = min(min_y, np.min(mesh.vertices[:, 1]))

# 平面 (plane) を作成
plane = trimesh.creation.box((10, 10, 0.01), origin=[0, 0, 0])
# print(min_y)

# 平面のy座標を最小のy座標に設定
plane.apply_translation([0,0 ,0.5])

# 平面を90度回転させる
rotation_matrix_plane = trimesh.transformations.rotation_matrix(np.pi / 2, [1, 0, 0])
plane.apply_transform(rotation_matrix_plane)

# メッシュのループ
for name, mesh in scene.geometry.items():
    if name in mesh_names_to_move:
        mesh.apply_translation(translation_vector)


# シーンに平面を追加
scene.add_geometry(plane)

# 移動後のシーンを表示
# scene.show()

rendered_image = scene.save_image()

# 画像をファイルに保存
with open(camera_positions["output_filename"], "wb") as image_file:
    image_file.write(rendered_image)
