import dicom, os, shutil, sys, glob

# input: directory with the DICOM files
# output: directory to store files organized by study UID

inputDir = sys.argv[1]
tag = sys.argv[2]

tags = {}

for root,dirnames,filenames in os.walk(inputDir):
  for filename in filenames:
    inputFile = os.path.join(root,filename)
    try:
      dcm = dicom.read_file(inputFile)  
    except:
      continue
    
    try:
      de = dcm.data_element(tag)
    except:
      print 'Failed to find ',tag,' in ',inputFile
      continue
    try:
      tags[de.value] += 1
    except:
      tags[de.value] = 1

print 'Tag: ',tag,' Values encountered: ',tags