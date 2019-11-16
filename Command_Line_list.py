# 1.Create folders names --> "path_to_checkpoints" & "path_to_predictions"
# 2.Verify dataset
# python -m keras_segmentation verify_dataset  --images_path="dataset1/images_prepped_train/" --segs_path="dataset1/annotations_prepped_train/"  --n_classes=50

# 3.Visualize dataset
# python -m keras_segmentation visualize_dataset  --images_path="dataset1/images_prepped_train/" --segs_path="dataset1/annotations_prepped_train/"  --n_classes=50

# 4.Train
# python -m keras_segmentation train --checkpoints_path="path_to_checkpoints" --train_images="dataset1/images_prepped_train/" --train_annotations="dataset1/annotations_prepped_train/" --val_images="dataset1/images_prepped_test/" --val_annotations="dataset1/annotations_prepped_test/" --n_classes=50 --input_height=320 --input_width=640 --model_name="vgg_unet"

# 5.Predict
# python -m keras_segmentation predict --checkpoints_path="path_to_checkpoints" --input_path="dataset1/images_prepped_test/" --output_path="path_to_predictions"