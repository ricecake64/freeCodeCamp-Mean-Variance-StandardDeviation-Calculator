import numpy as np

def calculate(list):
    #check if list length is valid
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    #convert list into 3x3 numpy array
    arr = np.array(list)
    new_arr = arr.reshape(3,3)

    #mean calculations
    mean_column_list = [new_arr[:,0].mean(), new_arr[:,1].mean(), new_arr[:,2].mean()]
    mean_row_list = [new_arr[0,:].mean(), new_arr[1,:].mean(), new_arr[2,:].mean()]
    new_arr_mean = new_arr.mean()
    mean_list = [[mean_column_list], [mean_row_list], new_arr_mean]

    #variance calculations
    variance_column_list = [new_arr[:,0].var(), new_arr[:,1].var(), new_arr[:,2].var()]
    variance_row_list = [new_arr[0,:].var(), new_arr[1,:].var(), new_arr[2,:].var()]
    new_arr_variance = new_arr.var()
    var_list = [[variance_column_list], [variance_row_list], new_arr_variance]

    #standard deviation calculations
    sd_column_list = [new_arr[:,0].std(), new_arr[:,1].std(), new_arr[:,2].std()]
    sd_row_list = [new_arr[0,:].std(), new_arr[1,:].std(), new_arr[2,:].std()]
    new_arr_sd = new_arr.std()
    sd_list = [[sd_column_list], [sd_row_list], new_arr_sd]

    #max calculations
    mx_column_list = [new_arr[:,0].max(), new_arr[:,1].max(), new_arr[:,2].max()]
    mx_row_list = [new_arr[0,:].max(), new_arr[1,:].max(), new_arr[2,:].max()]
    new_arr_mx = new_arr.max()
    mx_list = [[mx_column_list], [mx_row_list], new_arr_mx]

    #min calculations
    mn_column_list = [new_arr[:,0].min(), new_arr[:,1].min(), new_arr[:,2].min()]
    mn_row_list = [new_arr[0,:].min(), new_arr[1,:].min(), new_arr[2,:].min()]
    new_arr_mn = new_arr.min()
    mn_list = [[mn_column_list], [mn_row_list], new_arr_mn]

    #sum calculations
    sm_column_list = [new_arr[:,0].sum(), new_arr[:,1].sum(), new_arr[:,2].sum()]
    sm_row_list = [new_arr[0,:].sum(), new_arr[1,:].sum(), new_arr[2,:].sum()]
    new_arr_sm = new_arr.sum()
    sm_list = [[sm_column_list], [sm_row_list], new_arr_sm]

    #create dictionary
    calculations =  {
        'mean': mean_list,
        'variance': var_list,
        'standard deviation': sd_list,
        'max': mx_list,
        'min': mn_list,
        'sum': sm_list
    }

    return calculations
