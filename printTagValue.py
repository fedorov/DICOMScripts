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

if not os.path.exists(inputDir):
  print inputDir,' does not exist'
  abort

for root,dirnames,filenames in os.walk(inputDir):
  print root, dirnames, filenames
  for filename in filenames:
    print 'Reading ',filename
    inputFile = os.path.join(root,filename)
    try:
      dcm = dicom.read_file(inputFile)  
    except:
      print 'Failed to read ',inputFile
      continue
    
    try:
<<<<<<< Updated upstream
      if tagName:
        de = dcm.data_element(tagName)
      else:
        de = dcm[numericTag[0],numericTag[1]]
=======
      de = dcm.data_element(tag)
      print de.value
>>>>>>> Stashed changes
    except:
      print 'Failed to find ',tag,' in ',inputFile
      continue
    try:
      tags[str(de.value)] += 1
    except:
      tags[str(de.value)] = 1

print 'Tag: ',tag,' Values encountered: ',tags
