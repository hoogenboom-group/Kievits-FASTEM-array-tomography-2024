import webknossos as wk

def open_wk_dataset_seg_remote(dataset_full_url, EM_layer, segmentation, MAG_seg, MAG_EM, bbox_EM=None, bbox_seg=None) -> None:
    # open local dataset in given directory 
    dataset = wk.Dataset.open_remote(
        dataset_name_or_url=dataset_full_url
        )
    voxel_size = dataset.voxel_size

    EM = dataset.get_layer(EM_layer) # Layer
    labels = dataset.get_layer(segmentation) # Segmentation Layer
    mag_view = EM.get_mag(MAG_EM) # MagView
    mag_view_seg = labels.get_mag(MAG_seg) # MagView

    view = mag_view.get_view(absolute_offset=bbox_EM.topleft, size=bbox_EM.size) # "absolute_offset" and "size" are in Mag(1)!
    view_seg = mag_view_seg.get_view(absolute_offset=bbox_seg.topleft, size=bbox_seg.size) # "absolute_offset" and "size" are in Mag(1)!
    
    data = view.read()
    seg = view_seg.read()

    # return data, voxel size
    return dataset, data, seg, voxel_size

def import_wk_dataset_remote(dataset_full_url) -> None:
    # open remote dataset with dataset name, organization id and WebKnossos url 
    dataset = wk.Dataset.open_remote(
            dataset_name_or_url=dataset_full_url
            )
    voxel_size = dataset.voxel_size

    # return data, voxel size
    return dataset, voxel_size
