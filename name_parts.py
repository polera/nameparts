def defendant_name_parts(defendant_name):
    
    SALUTATIONS = ['MR','MS','MRS','DR','MISS']
    SUFFIXES    = ['JR','SR','ESQ','I','II','III','IV','V','VI','VII','VIII','IX','X','PHD']
    LNPREFIXES  = ['DE', 'DA', 'DI','LA', 'DU', 'DEL', 'DEI', 'VDA', 'DELLO', 'DELLA', 
                   'DEGLI', 'DELLE', 'VAN', 'VON', 'DER', 'DEN', 'HEER', 'TEN', 'TER', 
                   'VANDE', 'VANDEN', 'VANDER', 'VOOR', 'VER', 'AAN', 'MC', 'BEN','SAN',
                   'SAINZ']
    NON_NAME    = ['A.K.A.','AKA','A/K/A','F.K.A','FKA','F/K/A','R/A','C/O','N/K/A',
                   'N.A.','CORP.','CO.','INC','ASSOCIATES','SERVICE','LLC','FICTITIOUS']
    SUPPLEMENTAL_INFO = ['WIFE OF','HUSBAND OF','SON OF','DAUGHTER OF']

    name_parts  = {'salutation' :'',
                   'first_name' :'',
                   'middle_name':'',
                   'last_name'  :'',
                   'suffix'     :'',}
    
    # Just return on any AKA nonsense for now
    try:
        for non_name_text in NON_NAME:
            if defendant_name.upper().find(non_name_text) > -1:
                return (False, name_parts)
    except AttributeError:
        return (False, name_parts)
    

    # Only work to the left of any supplemenal non-name nonsense now
    for supplemental_text in SUPPLEMENTAL_INFO:
        supplemental_index = defendant_name.upper().find(supplemental_text)
        if supplemental_index > - 1:
            print defendant_name
            defendant_name = defendant_name[0:supplemental_index].replace(",","")
            print defendant_name
            
    defendant_name = defendant_name.replace(".","")    
    split_name = defendant_name.upper().split(' ')
    index = 0
    for part in split_name:
        if not part.isalpha():
            del split_name[index]
        index += 1
    # More than just a first and last name
    if len(split_name) > 2:
        if split_name[0] in SALUTATIONS:
            name_parts['salutation'] = split_name[0]
            del(split_name[0]) # Remove our salutation
            name_parts['first_name'] = split_name[0]  
            del(split_name[0]) # No need to hold on to the first name
            if split_name[-1] in SUFFIXES:
                name_parts['suffix']=split_name[-1]
                del(split_name[-1]) # No need to hold on to the suffix
            if len(split_name) > 1:
                if split_name[0] in LNPREFIXES:
                    name_parts['last_name'] = " ".join(split_name)
                    return (True, name_parts)
                else:
                    name_parts['middle_name'] = split_name[0]
                    del(split_name[0])
                    if split_name[0] in LNPREFIXES:
                        name_parts['last_name'] = " ".join(split_name)
                    else:
                        name_parts['last_name'] = "".join(split_name)
                    return (True, name_parts)
            else:
                name_parts['last_name'] = "".join(split_name)
                return (True, name_parts)
        else:
            name_parts['first_name'] = split_name[0]  
            del(split_name[0]) # No need to hold on to the first name
            if split_name[-1] in SUFFIXES:
                name_parts['suffix']=split_name[-1]
                del(split_name[-1]) # No need to hold on to the suffix
            if len(split_name) > 1:
                if split_name[0] in LNPREFIXES:
                    name_parts['last_name'] = " ".join(split_name)
                    return (True, name_parts)
                else:
                    name_parts['middle_name'] = split_name[0]
                    del(split_name[0])
                    if split_name[0] in LNPREFIXES:
                        name_parts['last_name'] = " ".join(split_name)
                    else:
                        name_parts['last_name'] = "".join(split_name)
                    return (True, name_parts)
            else:
                name_parts['last_name'] = "".join(split_name)
                return (True, name_parts)
            
    # Assume just a first and last name    
    elif len(split_name) == 2:
        if(split_name[0] in SALUTATIONS):
            return (False, name_parts)
        name_parts['first_name']= split_name[0]
        name_parts['last_name'] = split_name[1]
    else:
        return (False, name_parts)
    
    return (True, name_parts)

def run_tests():
    # Name tests
    name_tests = ["Mr. Michael J. Fox","Michael J. Fox","Mr. Michael J. Fox, Esq.",
                  "William Jefferson Clinton III","George H.W. Bush","George W. Bush",
                  "Thurston Howell III","Mickey Mouse a.k.a. Donald the Duck",
                  "Bank of America, N.A.","CITIBANK","Franco Harris","Hillary Rodham-Clinton",
                  "MR. RICHARDSON, HUSBAND OF DOROTHY RICHARDSON","William Sainz de Jeffries"]
    for name in name_tests:
        print defendant_name_parts(name)

if __name__ == "__main__":
    #run_parties()
    run_tests()
