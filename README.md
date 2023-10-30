# move_mesh2

meshの位置がバグる問題を改善したいです。  

初めにchair_dataset3.pkl.zipの解凍をお願いします。    

mesh_check.pyではデータセット内に含まれる各椅子のsceneに関する情報を調べられます。  
delete_other_legs.pyでは必要なmeshを一つのmeshにまとめる作業をしていますが、統合後のmeshの姿勢や位置がずれてしまいます。   
unstable_chairディレクトリ内ではそれぞれの椅子の上部をランダムな値で動かそうとしていますが、scene0のみ成功している状況で、scene1では部材ごとに動く幅が異なる問題、scene2ではそもそも動かない問題が発生しています。scene2のmesh_names_to_move内のmesh_nameはランダムに選んでいます。    

分かっていること  
・ 特定のmeshを削除しても他のmeshの位置が変わらない  
・ meshを一つづつ表示すると、位置と姿勢が全体を表示している時と変化する  
・ merged_mesh = trimesh.util.concatenate(meshes_to_merge)この関数で複数のmeshを統合すると位置がバグるmeshが存在する  
・ planeを追加しても椅子を構成するmeshの位置と姿勢に変化はない  
・ unstable_chair/scene_0.pyの41行目からコメントアウトしている部分で椅子の最下部の頂点を取得している。これは椅子の最下部にplaneを配置しようとしたためです。ここで取得したmin_yに従ってplaneを配置すると椅子と大きく離れた状態となるため。椅子をレンダリングする際に何らかのスケーリングがなされている可能性がある    

不明な点  
・dir（scene.geometry(mesh_name）)などを利用してmeshの相対位置情報と姿勢、カメラ情報を探したが見つけることができなかった  
