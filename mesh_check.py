import pickle
import trimesh

# データセットを読み込む
with open("chair_dataset3.pkl", "rb") as pickle_file:
    chair_dataset = pickle.load(pickle_file)

# 5番目のメッシュデータを取り出す
shape_id, style_id, shape_label, scene = chair_dataset[0]  # インデックスは0から始まるので、5番目はインデックス4

# scene.show()

# for name, mesh in scene.geometry.items():
#     print(name)
#     mesh.show()

#不要なメッシュを削除する，椅子の上部に該当
# meshes_to_remove = ["Mesh", "Mesh.001", "Mesh.011", "Mesh.012", "Mesh.013", "Mesh.014"]
meshes_to_remove = ["Mesh", "Mesh.001", "Mesh.002", "Mesh.003", "Mesh.004"]

# for mesh_name in meshes_to_remove:
#     if mesh_name in scene.geometry:
#         scene.delete_geometry(mesh_name)

# 統合されたメッシュを表示する
# scene = trimesh.Scene(merged_mesh)
# scene.show()

# print(dir(scene.geometry["Mesh"]))


# scene.show()


