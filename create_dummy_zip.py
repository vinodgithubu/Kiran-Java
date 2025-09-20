import zipfile

with zipfile.ZipFile('deployment-package.zip', 'w') as zipf:
    zipf.writestr('dummy.txt', 'This is a dummy file for Lambda deployment.')
print("Created deployment-package.zip with dummy.txt")