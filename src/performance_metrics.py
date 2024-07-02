from scipy.optimize import linear_sum_assignment as linear_assignment
import numpy as np

def separate_masks(all_masks):
    # Initialize a list to store masks for each instance
    separated_masks = []
    
    # Iterate over unique labels (instances)
    for label in np.unique(all_masks):
        if label == 0:
            # Skip background label
            continue
        
        # Extract mask for the current instance
        instance_mask = all_masks == label
        
        # Add the instance mask to the list
        separated_masks.append(instance_mask)
    
    return separated_masks

def compute_iou(pred_mask, gt_mask):
    intersection = np.logical_and(pred_mask, gt_mask)
    union = np.logical_or(pred_mask, gt_mask)

    return intersection.sum() / union.sum()

def compute_instance_iou(pred_mask, gt_mask, intersection, union):
    "Compute instance IoU without having to calculate over full array"
    return (intersection[pred_mask].sum() + intersection[gt_mask].sum()) / intersection[pred_mask].sum() + intersection[gt_mask].sum()

def match_instances(pred_masks, gt_masks, iou_matrix, IoU_thres=0.5):
    # Apply Hungarian algorithm
    print('Applying Hungarian algorithm...')
    row_ind, col_ind = linear_assignment(-iou_matrix)  # maximize
    
    # Initialize matches
    matches = []
    
    print('Finding matches...')
    # Threshold the assignments
    for i, j in zip(row_ind, col_ind):
        if iou_matrix[i, j] >= IoU_thres:
            matches.append((i, j))
            
    # Process matches and non-matches
    tp = len(matches) # true positives
    fp = len(pred_masks) - tp # false positives 
    fn = len(gt_masks) - tp
    
    return tp, fp, fn, matches

def compute_f1(tp, fp, fn):
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    return 2 * (precision * recall) / (precision + recall)

def compute_ap(tp, fp, fn):
    return tp / (tp + fp + fn)

def compute_iou_matrix(pred_masks, gt_masks):
    # Initialize IoU matrix
    num_pred = len(pred_masks)
    num_gt = len(gt_masks)
    iou_matrix = np.zeros((num_pred, num_gt), dtype=np.float64)
    
    # Compute IoU matrix
    print('Computing IoU matrix...')
    for i in range(num_pred):
        pred_mask = pred_masks[i]
        for j in range(num_gt):
            gt_mask = gt_masks[j]
            intersection = np.logical_and(pred_mask, gt_mask)
            union = np.logical_or(pred_mask, gt_mask)
            iou = intersection.sum() / union.sum()
            iou_matrix[i, j] = iou
    return iou_matrix

