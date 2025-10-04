import pyimzml.ImzMLParser as ImzMLParser
import matplotlib.pyplot as plt
import matplotlib as mpl
import warnings
import numpy as np
import os
import imzml_writer.utils as iw_utils
import time
import cv2 as cv
import scipy.ndimage
import matplotlib.colors as mcolors
# from lamp import anno, stats, utils



def annotate_by_mz_list(mz:list[float],tolerance:float=5):
    pass

def convert_from_RAW(dir:str,mode:str="Centroid",x_speed:float=40.0,y_step:float=150.0,filetype:str="raw", stop_at_mzML:bool=False):
    """Placeholder"""
    iw_utils.RAW_to_mzML(dir,write_mode=mode,blocking=True)

    iw_utils.clean_raw_files(dir,filetype)
    if stop_at_mzML:
        return
    mzML_path = os.path.join(dir,"Output mzML Files")
    iw_utils.mzML_to_imzML_convert(PATH=mzML_path)

    iw_utils.imzML_metadata_process(
        model_files=mzML_path,
        x_speed=x_speed,
        y_step=y_step,
        path=dir
        )
    

def get_image_matrix(src:str, mz:list | float = 104.1070,tol: list | float = 10.0):
    """Retrieves the requested ion image as a numpy array
    
    :param src: File path to the imzML source
    :param mz: m/z or list of m/z to retrieve images for
    :param tol: Tolerance with which to retrieve the images"""

    with warnings.catch_warnings(action="ignore"):
        with ImzMLParser.ImzMLParser(filename=src,parse_lib='lxml') as img:
            if isinstance(mz,float):
                tolerance = mz * tol / 1e6
                img_raw = ImzMLParser.getionimage(img, mz, tolerance)
            elif isinstance(mz,list):
                img_raw = []
                for idx, spp in enumerate(mz):
                    if isinstance(tol,float) or isinstance(tol,int):
                        tolerance = spp * tol / 1e6
                    elif isinstance(tol,list):
                        tolerance = spp * tol[idx] / 1e6
                    img_raw.append(ImzMLParser.getionimage(img,spp,tolerance))
                
    return img_raw


def get_TIC_image(src:str):
    """Placeholder"""
    with warnings.catch_warnings(action='ignore'):
        with ImzMLParser.ImzMLParser(filename=src,parse_lib='lxml') as img:
            tic_image = ImzMLParser.getionimage(img,500,9999)
    
    return tic_image

def get_weighted_median_image(src:str):

    def wmi_reduce_func(seq):
        no_zeros = seq[seq!=0]
        return np.median(no_zeros)

    with warnings.catch_warnings(action='ignore'):
        with ImzMLParser.ImzMLParser(filename=src, parse_lib='lxml') as img:
            wmi = ImzMLParser.getionimage(img,500,9999,reduce_func=wmi_reduce_func)  
    
    return wmi


def get_scale(src:str):
    """Returns the dimensions of the image in µm
    :param src: Path to the imzML
    :return: Tuple of form (scale_x, scale_y)"""
    with warnings.catch_warnings(action="ignore"):
        img = ImzMLParser.ImzMLParser(filename=src,parse_lib='lxml')
        metadata = img.metadata.pretty()
        scan_settings = metadata["scan_settings"]["scanSettings1"]
        for key in scan_settings.keys():
            if key == "max dimension x":
                scale_x = scan_settings[key]
            elif key == "max dimension y":
                scale_y = scan_settings[key]
        return scale_x, scale_y

def get_aspect_ratio(src:str):
    """Placeholder"""
    with warnings.catch_warnings(action="ignore"):
        img = ImzMLParser.ImzMLParser(filename=src,parse_lib='lxml')
        metadata = img.metadata.pretty()
        scan_settings = metadata["scan_settings"]["scanSettings1"]
        for key in scan_settings.keys():
            if key == "pixel size (x)" or key == "pixel size x":
                x_pix = scan_settings[key]
            elif key == "pixel size y":
                y_pix = scan_settings[key]
        
        return y_pix / x_pix


def draw_ion_image(data:np.array, cmap:str="viridis",mode:str = "draw", path:str = None, cut_offs:tuple=(5, 95),quality:int=100, asp:float=1,scale:float=1,NL_override=None, custom_size:tuple=None):
    """Placeholder"""
    mpl.rcParams['savefig.pad_inches'] = 0
    up_cut = np.percentile(data,max(cut_offs))
    down_cut = np.percentile(data,min(cut_offs))

    img_cutoff = np.where(data > up_cut,up_cut,data)
    img_cutoff = np.where(data < down_cut,0,data)

    fig = plt.figure()
    _plt = plt.subplot()
    _plt.axis('off')
    if NL_override == None:
        _plt.imshow(img_cutoff,aspect=asp,interpolation="none",cmap=cmap,vmax=up_cut,vmin=0)
    else:
        _plt.imshow(img_cutoff,aspect=asp,interpolation="none",cmap=cmap,vmax=NL_override,vmin=0)
    size = fig.get_size_inches()
    scaled_size = size * scale
    fig.set_size_inches(scaled_size)

    if custom_size:
        fig.set_size_inches(custom_size)


    if mode == "draw":
        plt.show()
    elif mode == "save":
        if path is None:
            raise Exception("No file name specified")
        else:
            fig.savefig(path, dpi=quality,pad_inches=0,bbox_inches='tight')
            plt.close(fig)
    
def unsharp_mask(image, kernel_size=(5, 5), sigmaX=1.0, sigmaY=1.0, amount=1.0, threshold=0):
    """Return a sharpened version of the image, using an unsharp mask."""
    blurred = cv.GaussianBlur(image, kernel_size, sigmaX=sigmaX, sigmaY=sigmaY)
    sharpened = float(amount + 1) * image - float(amount) * blurred
    sharpened = np.maximum(sharpened, np.zeros(sharpened.shape))
    sharpened = np.minimum(sharpened, np.max(image) * np.ones(sharpened.shape))
    # sharpened = sharpened.round().astype(np.uint8)
    if threshold > 0:
        low_contrast_mask = np.absolute(image - blurred) < threshold
        np.copyto(sharpened, image, where=low_contrast_mask)
    return sharpened

def smooth_image(img_data,asp:float, factor:int=3,base_sigma:float=10,weight_factor:float=0.5):
    zoomed_img = scipy.ndimage.zoom(img_data,factor)
    sharpened_img = unsharp_mask(zoomed_img, sigmaX=base_sigma, sigmaY=base_sigma/asp, kernel_size=(9,9), amount=weight_factor)
    return sharpened_img


def find_matching_ROI(ROI_files:list,match_folder:str, ROI_folder:str):
    matching_npz = None

    if f"{match_folder}.npz" in ROI_files:
        matching_npz = os.path.join(ROI_folder, f"{match_folder}.npz")
        all_data = np.load(matching_npz)
        roi_mask = all_data['roi_mask']
        return roi_mask

    for file in ROI_files:
        file_string = file.split(".npz")[0]
        if file_string in match_folder:
            matching_npz = os.path.join(ROI_folder, file)
            break
    
    if matching_npz is not None:
        all_data = np.load(matching_npz)
        roi_mask = all_data['roi_mask']
        return roi_mask
    else:
        print(f"No matching file found! folder name: {match_folder}")
        raise
        
            

def find_data_filt_string(path:str, search_pattern:str):
    bad_options = ["Initial RAW files", "Output mzML Files"]
    top_files = os.listdir(path)
    for candidate in top_files:
        if os.path.isdir(os.path.join(path, candidate)):
            if not candidate.startswith(".") and candidate not in bad_options:
                working_folder = os.path.join(path,candidate)
                break
        elif candidate.endswith(search_pattern):
            return os.path.join(path, candidate)
        
    for file in os.listdir(working_folder):
        if search_pattern in file:
            return os.path.join(working_folder,file)


def grid_image(dir:str, dims:tuple=None,names:list=None,ext:str=".tif", title_string:str=None, savepath:str=None, cbar_cutoffs:tuple=(5, 95)):
    """Takes in a folder of images and makes a grid from them to display them all at once.
    
    :param dims: Tuple of form height, width"""
    all_images = [image for image in os.listdir(dir) if image.endswith(ext)]
    all_images = [image for name in names for image in all_images if name in image]

    fig, axarr = plt.subplots(dims[0], dims[1])
    fig.set_size_inches(dims[1]*1.5,dims[0]*1.5)
    fig.set_facecolor("#440154")
    my_axes = axarr.ravel()

    for idx, image in enumerate(all_images):
        local_img = plt.imread(os.path.join(dir,image))
        my_axes[idx].imshow(local_img)
        my_axes[idx].set_title(names[idx], color='white')
        my_axes[idx].set_axis_off()
    
    ticker = 0
    while idx < len(my_axes)-1:
        ticker +=1
        idx += 1
        my_axes[idx].set_axis_off()
        my_axes[idx].set_facecolor("#440154")
        if ticker==1:
            my_axes[idx].text(0.5, 0.5, title_string, color='white', weight='bold', ha='center', va='center')
        if ticker==2:
            plt.tight_layout()
            norm = mcolors.Normalize(vmin=0, vmax=100)
            ax_pos = my_axes[idx].get_position()
            width = 0.2
            height = 0.7
            cbar_position = [ax_pos.x0 + 0.05, ax_pos.y0, ax_pos.width * width, ax_pos.height * height]
            cbar_ax = fig.add_axes(cbar_position)  # Add the colorbar axes at the defined position
            cbar = fig.colorbar(
                plt.cm.ScalarMappable(norm=norm, cmap='viridis'),
                cax=cbar_ax,
                orientation='vertical'
            )
            cbar.set_label('Intensity', color='white', rotation=270, va='center')  # Set your label if needed
            cbar.ax.yaxis.set_tick_params(color='white')  # Set color for colorbar ticks
            cbar.ax.yaxis.set_ticks_position('left')
            cbar.set_ticks([0, 100])
            cbar.set_ticklabels([f"{cbar_cutoffs[0]}th", f"{cbar_cutoffs[1]}th"])
            cbar.ax.set_yticklabels(cbar.ax.get_yticklabels(), color='white')  # Set tick labels to white
    
    if not savepath:
        plt.show()
    else:
        plt.savefig(savepath)
        plt.close()





def bulk_image_export(dir:str,search_pattern:str, save_path:str, mz_list:list, target_list:list, include_codes:list=None, tolerance:float=10, uniform_scale:bool=False,smooth:bool=False,universal_cutoff:float=80, ROI_files:list=None, ROI_path:str=None):
    """Convenient API to convert a folder full of imzML files into ion images for a provided list of metabolites.
    
    :param dir: Path to the directory containing the imzML files (organized by experiment - each one in its own subfolder)
    :param search_pattern: Search string for the scan filter at the end of the imzML
    :param save_path: Path to a folder where images should be saved.
    :param mz_list: List of m/z to generate images for
    :param target_list: List of names matching the m/z list
    :param include_codes: List of strings that must be included to produce an output (when you want to subset a larger campaign)
    :param tolerance: Tolerance (in ppm) with which to extract the images
    :param uniform_scale: Optional argument for whether images should be scaled to self (False; default) or normalized to the most intense image (True)
    :param smooth: Should the resulting images be smoothed
    :param universal_cutoff: Fudge factor for the uniform_scaling - where should the intensity cutoff percentile be
    :param ROI_files: List of ROI filenames to match with folder names (based on sample codes for example) if image should only show a subset of pixels
    :param ROI_path: Path where the ROI files are located"""

    roi_mask = None
    all_folders = os.listdir(dir)
    data_folders = []
    for folder in all_folders:
        if not folder.startswith("."):
            if not include_codes:
                data_folders.append(folder)
            elif any(code.lower() in folder.lower() for code in include_codes):
                data_folders.append(folder)
    
    for target in target_list:
        path = os.path.join(save_path, "images", target)
        os.makedirs(path, exist_ok=True)
    
    scale = None
    NLs = [0 for _ in range(len(mz_list))]

    data_list = []
    asp_list = []
    TIC_list = []
    scale_list = []
    roi_list = []
    real_dims = [] #Actual image dimensions to draw in inches

    #Check all the scales etc. - hold the data in memory so you don't have to retrieve fresh
    for file_idx, folder in enumerate(data_folders):
        print(f"Starting file {file_idx+1} / {len(data_folders)} - {folder}")
        image = find_data_filt_string(os.path.join(dir,folder),search_pattern=search_pattern)
        aspect_ratio = get_aspect_ratio(image)
        data = get_image_matrix(image, mz_list,tol=tolerance)
        TIC_image = get_TIC_image(image)

        if ROI_path is not None and ROI_files is not None:
            roi_mask = find_matching_ROI(ROI_files, folder, ROI_path)

        ##TODO Fix y-scaling too so they actually come out to scale!
        x_scale, y_scale = get_scale(image)
        if scale == None:
            scale = 1
            full_scale_x = 1
            full_scale_y = 1
            norm_factor = x_scale
        else:
            scale = x_scale / norm_factor
        
        for idx, img in enumerate(data):
            normalized = np.divide(img, TIC_image, out=np.zeros_like(img), where=TIC_image!=0)
            if roi_mask is not None:
                normalized = normalized * roi_mask
            
            top_cutoff = np.percentile(normalized, universal_cutoff)
            if top_cutoff > NLs[idx]:
                NLs[idx] = top_cutoff

        data_list.append(data)
        asp_list.append(aspect_ratio)
        TIC_list.append(TIC_image)
        scale_list.append(scale)
        roi_list.append(roi_mask)
        real_dims.append((x_scale/2540, y_scale/2540))

    print("Saving images...")
    for file_idx, folder in enumerate(data_folders):
        data = data_list[file_idx]
        aspect_ratio = asp_list[file_idx]
        TIC_image = TIC_list[file_idx]
        scale = scale_list[file_idx]
        roi_mask = roi_list[file_idx]

        for idx, img in enumerate(data):
            path = os.path.join(save_path,"images",target_list[idx], f"{folder}-{target_list[idx]}.tif")
            normalized = np.divide(img, TIC_image, out=np.zeros_like(img), where=TIC_image!=0)

            if roi_mask is not None:
                normalized = normalized * roi_mask

            if smooth:
                normalized = smooth_image(normalized, aspect_ratio, factor=10)
            
            
            if uniform_scale:
                draw_ion_image(normalized, 'viridis', mode='save', path=path, asp=aspect_ratio, cut_offs=(20, 95), scale=scale, NL_override=NLs[idx], custom_size=real_dims[file_idx])
            else:
                draw_ion_image(normalized, cmap='viridis', mode='save', path=path, asp=aspect_ratio, cut_offs=(20, 95), scale=scale, custom_size=real_dims[file_idx])






        





    
