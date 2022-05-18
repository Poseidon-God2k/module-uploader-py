# from datetime import datetime
# from db_uploader.schema.schedule import UploadVehicleInfo,UploadImage
# from db_uploader.uploader import save_vehicle_info

# plate_recognize = {
#     "camera_id": "6173c8d52edc4b6a2898b4e7",
#     "list_vehicle_images": [
#          {
#             "image": "data:image/png;base64,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",
#             "folder":"test1"
#         }
#     ],
#     "list_plate_images": [
#         {
#             "image": "data:image/png;base64,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",
#             "folder":"test1"
#         },
#         {
#             "image": "data:image/png;base64,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",
#             "folder":"test1"
#         }
#     ],
#     "plate": "123456",
#     "possible_plates": [
#         {
#             "predict": "123456",
#             "accurate": 0.78
#         },
#         {
#             "predict": "78910",
#             "accurate": 0.79
#         },
#     ],
#     "vehicle_type": "MOTORCYCLE",
#     "record_time": datetime.now(),
#     "start_frame": 1,
#     "end_frame": 200,
#     "preview_image": {
#         "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAABuwAAAbsBOuzj4gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAALJSURBVHic7Zs9T1NRHMaf0/vS3ktbEApD1UhiUhcSQ8JCXFxonaSLiX4B44hMDI5OLDIav4IJAyF8Ah0cCYsOJBAVykuRFijlttzjUAMRSFug5zxDzy9p0tuc5j7n1/Py72kqpJToZiLsAGyMAHYANkYAOwAbI4AdgI0RwA7ARvxA5iU7BBPxHY+6uhbu+ilgBLADsDEC2AHYGAHsAGyoAoTVeDChCvDHY/DHY8wIsJk3j+c8AMDRlyotA28EWEBiwkdiwgeI04AmwB+LwuqPwOqPwB+LsmLwBCSe+Vc+1w1HgADiWe/sMp71AEFJwhHgjUZhD55PfHvQgjfKmQYUAYmc19ZrOuj4Nph87sN/0nxvjz+93NlkvgeRvuafR+VrFeWFyq3yXaTzJ0IC6H+dRGqqt2NVnjwFdudK2PtUBjp8fqXsSCz22EX6wwCce7cbZLVfdWy8LaK6HHQo2f8oWwOqywHWJrdwsHTzIXuwVMHa5JayzgOaDkV7X/Rg6N0dRLz29rrwWGL7/R+UPh8pTqbxVNh96ODuxxTcB82nRLBex+83uwhWazpi6dsGg9Ua5Elr1/JEaus8oFGAO2wjmnFatotmHLjD+r6kahMQz7Vf71+n7W3RJuBipSfrEjuz+9iZ3Yesy6ZtVaJlrDlpC7ER9+y69rOOjakiqiuN7a3y7QTpuQE49xtxYiMunLSF2sap8mxaRkA8ez6ky4v/9vaV8729utKoGcqLlSvfoxItAhJZD+GxRGFmD5vTRYSH4aU24WGIzekiCjN7CI8lElk900C5ADtlQXgC6/kCSvOtC5vS/BHW8wUIT8BOqT8rU14I2UMWTvdDyOB6txGugNUXQX1b7TqgfBG8aQdkIJV3HjC/DBkBRgA7ABsjgB2AjRHADsCm6wXYAvIVOwQTYf411uUYAewAbIwAdgA2RgA7ABsjgB2AzV8BuL82qoSbHQAAAABJRU5ErkJggg==",
#         "folder":"preview"
#     }
# }

# video_record = {
#     "video_url": "bkel sap cmnr",
#     "duration": 34567,
#     "camera_id": "6173c8d52edc4b6a2898b4e7"
# }

# uploadInfo = UploadVehicleInfo(
#     vehicle_images= [UploadImage(plate_recognize["list_vehicle_images"][0]["image"], "test1")],
#     lp_images= [UploadImage(plate_recognize["list_plate_images"][0]["image"], "test1"), UploadImage(plate_recognize["list_plate_images"][0]["image"], "test1")],
#     lp_labels= [{"label": "084852"}],
#     record_time = datetime.now(),
#     start_frame= 1,
#     end_frame= 1,
#     preview_image = UploadImage(plate_recognize["preview_image"]["image"], "preview"),
#     camera_id= "6173c8d52edc4b6a2898b4e7",
#     type= "Truck",
# )


# save_vehicle_info(uploadInfo, "12234555")

from uploader import upload_detected_vehicles
import pickle
file = open(
    "./db_uploader/data_test/congtruongnguyenhue_02h19m47s_recordvideo.pkl", 'rb')
file2 = open(
    "./db_uploader/data_test/congtruongnguyenhue_02h19m47s_vehicleinfos.pkl", 'rb')
data_video_record = pickle.load(file)
data_vehicle_infos = pickle.load(file2)

# print(data_vehicle_infos[0])


upload_detected_vehicles(data_vehicle_infos, data_video_record)
# from db_uploader.schema.schedule import UploadVehicleInfo, UploadVideoInfo

# data_video = UploadVideoInfo()