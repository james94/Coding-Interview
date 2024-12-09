import brain_region_analysis as bra

def create_sample_tree():
    root = bra.TreeNode(100)
    root.left = bra.TreeNode(50)
    root.right = bra.TreeNode(150)
    root.left.left = bra.TreeNode(30)
    root.left.right = bra.TreeNode(70)
    root.right.right = bra.TreeNode(180)
    return root

root = create_sample_tree()
low, high = 70, 150

try:
    result = bra.analyze_brain_regions(root, low, high)
    print(f"Sum of intensities in range [{low}, {high}]: {result}")
    print("This quantification helps identify and measure regions of interest in the brain MRI.")
except Exception as e:
    print(f"Error in analysis: {str(e)}")
