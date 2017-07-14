import numpy as np
import nibabel
import argparse
import json


parser = argparse.ArgumentParser(description='Compare images using Jaccard Index')
parser.add_argument('--test', required=True, help='input test image')
parser.add_argument('--truth', required=True, help='input truth image')

args = parser.parse_args()

MyTestImage = args.test
MyTruthImage = args.truth

nib_TestImg = nibabel.load(MyTestImage)
nib_TruthImg = nibabel.load(MyTruthImage)

TestImg = nib_TestImg.get_data()
TruthImg = nib_TruthImg.get_data()

TestImg = TestImg.astype(np.bool)
TruthImg = TruthImg.astype(np.bool)

intersection = np.logical_and(TestImg, TruthImg)
union = np.logical_or(TestImg, TruthImg)

jaccard = intersection.sum() / float(union.sum())

print (json.dumps({'Jaccard': jaccard}))


