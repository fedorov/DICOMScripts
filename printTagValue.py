import dicom, os, shutil, sys, glob

# input: directory with the DICOM files and a tag to look for
# output: values of tags encountered

if len(sys.argv)<3:
  print 'Usage: ',sys.argv[0],' inputDirectory tag'
  exit()

inputDir = sys.argv[1]
tag = sys.argv[2]

tagName = None
numericTag = None

if tag.find(',')>0:
  numericTag = [int(tag.split(',')[0],16),int(tag.split(',')[1],16)]
else:
  tagName = tag

tags = {}

for root,dirnames,filenames in os.walk(inputDir):
  for filename in filenames:
    inputFile = os.path.join(root,filename)
    try:
      dcm = dicom.read_file(inputFile)  
    except:
      continue
    
    try:
      if tagName:
        de = dcm.data_element(tagName)
      else:
        de = dcm[numericTag[0],numericTag[1]]
    except:
      print 'Failed to find ',tag,' in ',inputFile
      continue
    try:
      tags[de.value] += 1
    except:
      tags[de.value] = 1

print 'Tag: ',tag,' Values encountered: ',tags
