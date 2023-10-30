import pickle
import trimesh

# データセットを読み込む
with open("chair_dataset.pkl", "rb") as pickle_file:
    chair_dataset = pickle.load(pickle_file)

shape_id, style_id, shape_label, scene = chair_dataset[0]
# print(dir(scene.geometry))

# for i, scene_name in enumerate(scene.geometry):
#     print(f"Geometry {i}:")
#     print(scene_name)
#     print(type(scene.geometry[scene_name]))
    # scene.geometry[scene_name].show()
    #print(dir(scene.geometry[scene_name].visual))

# # print(dir(scene))

# #scene.show()


# mesh6, mesh7, mesh8をリストにまとめ
meshes_to_merge = [scene.geometry[f"Mesh.00{i}"] for i in range(6, 9)]
meshes_to_merge.append(scene.geometry["Mesh"])
meshes_to_merge.append(scene.geometry["Mesh.001"])

# メッシュを統合する
merged_mesh = trimesh.util.concatenate(meshes_to_merge)

# 統合されたメッシュを表示する
scene_merged = trimesh.Scene(merged_mesh)
scene_merged.show()


