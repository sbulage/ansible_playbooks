def subnet_name_filter(list, res_tag_name):
  list_subnets=[]
  #for filt_def in res_tag_name:
  #  list_subnets.append(subnet['id'] for subnet in list if subnet['resource_tags']['Name'] == filt_def)
    #print (subnet)
  return [ x['id'] for x in list if x['resource_tags']['Name'] in res_tag_name ]
  #return list_subnets

class FilterModule(object):
  def filters(self):
    return {          
      'subnet_name_filter': subnet_name_filter
    }
