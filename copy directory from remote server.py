# Create the destination dir if its not there. 
#if not os.path.exists(dest_dir): 
#    os.makedirs(dest_dir) 
#else: 
#    # Create a directory anyway if file exists so as to raise an error. 
#     if not os.path.isdir(dest_dir): 
#         os.makedirs(dest_dir) 
 
if move: 
    if os.path.isdir(source): 
        shutil.copytree(source, destdir) 
        shutil.rmtree(source) 
    elif os.path.isfile(source): 
        shutil.move(source, dest_dir) 
    else: 
        raise AssertionError, '%s is neither a file nor directory' % (source) 
else: 
    if os.path.isdir(source): 
        shutil.copytree(source, dest_dir) 
    elif os.path.isfile(source): 
        shutil.copy(source, dest_dir) 
    else: 
        raise AssertionError, '%s is neither a file nor directory' % (source) 
