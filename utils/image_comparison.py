import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim

def compare_images(path1, path2):
    # 1. Load Images
    img1 = cv2.imread(path1)
    img2 = cv2.imread(path2)

    if img1 is None or img2 is None:
        raise ValueError("Invalid Image Path or Image Not Found!")

    # --- Method 1: Structural Similarity (SSIM) ---
    # Good for: Exact duplicates, slight noise
    try:
        # Convert to grayscale
        gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

        # Resize to same dimensions for SSIM (using img1's size)
        height, width = gray1.shape
        gray2_resized = cv2.resize(gray2, (width, height))

        ssim_score = ssim(gray1, gray2_resized) * 100
    except Exception as e:
        print(f"SSIM Error: {e}")
        ssim_score = 0

    # --- Method 2: ORB Feature Matching ---
    # Good for: Rotated images, zoomed images, different lighting
    try:
        orb = cv2.ORB_create()
        
        # Find keypoints and descriptors
        kp1, des1 = orb.detectAndCompute(img1, None)
        kp2, des2 = orb.detectAndCompute(img2, None)
        
        # Match descriptors using BFMatcher
        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        matches = bf.match(des1, des2)
        
        # Sort matches by distance (best matches first)
        matches = sorted(matches, key=lambda x: x.distance)
        
        # Calculate score based on the number of good matches
        # If we find > 50 good matches, it's likely the same object
        # We normalize this to a 0-100 scale logic
        max_matches = min(len(kp1), len(kp2))
        if max_matches == 0:
            orb_score = 0
        else:
            orb_score = (len(matches) / max_matches) * 100
            
    except Exception as e:
        print(f"ORB Error: {e}")
        orb_score = 0

    # --- FINAL DECISION ---
    # We take the higher of the two scores. 
    # If it's a rotated duplicate, SSIM is low but ORB is high -> We return ORB.
    final_score = max(ssim_score, orb_score)
    
    return round(final_score, 2)