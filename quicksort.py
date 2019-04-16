
def partitioner(items_to_sort, first_item, last_item):
    
    pivot = items_to_sort[first_item]
    left_point = first_item + 1
    right_point = last_item

    done = False
    while not done:

        while left_point <= right_point and items_to_sort[left_point] <= pivot:
            # if the item on the left is smaller than the pivot, move the left_point across (i.e ignore it)
               left_point = left_point + 1

                    
        while items_to_sort[right_point] >= pivot and right_point >= left_point:
               right_point = right_point -1
            # likewise, if the point on the right is bigger than the pivot, just close the right in towards the middle

        if right_point < left_point:
               done = True
        else:
            # switch them round
            temp_store = items_to_sort[left_point]
            items_to_sort[left_point] = items_to_sort[right_point]
            items_to_sort[right_point] = temp_store

    temp_store = items_to_sort[first_item]
    items_to_sort[first_item] = items_to_sort[right_point]
    items_to_sort[right_point] = temp_store


    return right_point
        
        
def actual_quick_sort(items_to_sort, first_item, last_item):
        if first_item < last_item:
            # this is our base case - once the first_item is the same as the last_item the recursion will stop.
            
            divider = partitioner(items_to_sort, first_item, last_item)
            
            actual_quick_sort(items_to_sort,first_item,divider-1)
            actual_quick_sort(items_to_sort,divider+1,last_item)
            
            
def sortMe(items_to_sort):
    actual_quick_sort(items_to_sort, 0, len(items_to_sort)-1)
    return items_to_sort
    


test_dictionary = {24874.96981582321: ['LHR', 'JFK', 'SVO', 'SXF', 'XDB', 'LHR'],
 26042.673142630345: ['LHR', 'JFK', 'SVO', 'XDB', 'SXF', 'LHR'],
 23859.16815747754: ['LHR', 'JFK', 'SXF', 'SVO', 'XDB', 'LHR'],
 25057.86768395719: ['LHR', 'JFK', 'XDB', 'SVO', 'SXF', 'LHR'],
 23525.598640393408: ['LHR', 'JFK', 'XDB', 'SXF', 'SVO', 'LHR'],
 16951.456927844873: ['LHR', 'SVO', 'JFK', 'SXF', 'XDB', 'LHR'],
 16992.65409086306: ['LHR', 'SVO', 'JFK', 'XDB', 'SXF', 'LHR'],
 24255.19860230236: ['LHR', 'SVO', 'SXF', 'JFK', 'XDB', 'LHR'],
 23487.316314025706: ['LHR', 'SVO', 'SXF', 'XDB', 'JFK', 'LHR'],
 25363.079044601403: ['LHR', 'SVO', 'XDB', 'JFK', 'SXF', 'LHR'],
 24673.645362322746: ['LHR', 'SVO', 'XDB', 'SXF', 'JFK', 'LHR'],
 24162.016760295166: ['LHR', 'SXF', 'JFK', 'SVO', 'XDB', 'LHR'],
 23970.147948326823: ['LHR', 'SXF', 'JFK', 'XDB', 'SVO', 'LHR'],
 13589.46109991411: ['LHR', 'SXF', 'SVO', 'JFK', 'XDB', 'LHR'],
 21251.826649883893: ['LHR', 'SXF', 'SVO', 'XDB', 'JFK', 'LHR'],
 23768.624358702942: ['LHR', 'SXF', 'XDB', 'JFK', 'SVO', 'LHR'],
 15165.410223395957: ['LHR', 'SXF', 'XDB', 'SVO', 'JFK', 'LHR'],
 22512.437324399085: ['LHR', 'XDB', 'JFK', 'SVO', 'SXF', 'LHR'],
 21121.868985951096: ['LHR', 'XDB', 'JFK', 'SXF', 'SVO', 'LHR'],
 15410.219239565478: ['LHR', 'XDB', 'SVO', 'JFK', 'SXF', 'LHR'],
 21964.704347236217: ['LHR', 'XDB', 'SVO', 'SXF', 'JFK', 'LHR'],
 23323.999692593807: ['LHR', 'XDB', 'SXF', 'JFK', 'SVO', 'LHR'],
 12376.95414552832: ['LHR', 'XDB', 'SXF', 'SVO', 'JFK', 'LHR']
 }


dictionary_list = [key for key in test_dictionary]




print(sortMe(dictionary_list))