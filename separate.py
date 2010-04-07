class Address:
  pass

class Name:
   
  SALUTATIONS = ['MR','MS','MRS','DR','MISS']
  SUFFIXES    = ['JR','SR','ESQ','I','II','III','IV','V','VI','VII','VIII','IX','X','PHD']
  LNPREFIXES  = ['DE', 'DA', 'DI','LA', 'DU', 'DEL', 'DEI', 'VDA', 'DELLO', 'DELLA', 
                 'DEGLI', 'DELLE', 'VAN', 'VON', 'DER', 'DEN', 'HEER', 'TEN', 'TER', 
                 'VANDE', 'VANDEN', 'VANDER', 'VOOR', 'VER', 'AAN', 'MC', 'BEN','SAN',
                 'SAINZ']
  NON_NAME    = ['A.K.A.','AKA','A/K/A','F.K.A','FKA','F/K/A','N/K/A','FICTITIOUS']
  CORP_ENTITY = ['N.A.','CORP.','CO.','INC','ASSOCIATES','SERVICE','LLC','LLP','PARTNERS','R/A','C/O']
  SUPPLEMENTAL_INFO = ['WIFE OF','HUSBAND OF','SON OF','DAUGHTER OF']

  def get_has_non_name_values(self):
    try:
      for non_name_text in self.NON_NAME:
        if self.__full_name.upper().find(non_name_text) > -1:
          return True
    except AttributeError:
      pass
    return False
  has_non_name_values = property(get_has_non_name_values)
  
  def get_has_supplemental_info(self):
    try:
      for supplemental_info in self.SUPPLEMENTAL_INFO:
        if self.__full_name.upper().find(supplemental_info) > -1:
          return True
    except AttributeError:
      pass
    return False
  has_supplemental_info = property(get_has_supplemental_info)
  
  def get_has_salutation(self):
    if self.__split_name[0].upper() in self.SALUTATIONS:
      return True
    return False
  has_salutation = property(get_has_salutation)

  def get_has_suffix(self):
    if self.__split_name[-1].upper() in self.SUFFIXES:
      return True
    return False
  has_suffix = property(get_has_suffix)
      
  def __clean(self):
    unwanted = ['.',',','/']
    for char in unwanted:
      self.__full_name = self.__full_name.replace(char,'')
    for supplemental_text in self.SUPPLEMENTAL_INFO:
      supplemental_index = self.__full_name.upper().find(supplemental_text)
      if supplemental_index > -1:
        self.__full_name = self.__full_name[0:supplemental_index]
    self.__split_name = self.__full_name.split(" ")
  def __repr__(self):
    return unicode("<separate.Name: '%s'>" % self.__full_name)
      
  def process_name(self):  
    if self.__processed:
      return
    self.__clean()
    name_parts = self.__split_name
    
    # Find salutation, save it, remove it
    if self.has_salutation:
      self.__salutation = name_parts[0]
      del name_parts[0]

    # Find suffix, save it, remove it
    if self.has_suffix:
      self.__suffix = name_parts[-1]
      del name_parts[-1]
    
    # Save first name, remove it
    self.__first_name = name_parts[0]
    del name_parts[0]
    
    # The rest...
    if len(name_parts) > 1 and \
       name_parts[0].upper() not in self.LNPREFIXES:
      self.__middle_name = name_parts[0]
      del name_parts[0]
      self.__last_name = " ".join(name_parts)
    else:
      self.__last_name = " ".join(name_parts)
    self.__processed = True
    return
  
  def __init__(self, name):
    self.__full_name    = name
    self.__split_name   = []
    self.__salutation   = None
    self.__first_name   = None
    self.__middle_name  = None
    self.__last_name    = None
    self.__suffix       = None
    self.__processed    = False
    self.process_name()
    
  def get_full_name(self):
    return self.__full_name
  full_name = property(get_full_name)
  
  def get_salutation(self):
    return self.__salutation
  salutation = property(get_salutation)
  
  def get_first_name(self):
    return self.__first_name
  first_name = property(get_first_name)
  
  def get_middle_name(self):
    return self.__middle_name
  middle_name = property(get_middle_name)
  
  def get_last_name(self):
    return self.__last_name
  last_name = property(get_last_name)
  
  def get_suffix(self):
    return self.__suffix
  suffix = property(get_suffix)
  
  def get_name_as_dict(self):
    return {'salutation': self.salutation, 
            'first_name': self.first_name, 
            'last_name': self.last_name, 
            'middle_name': self.middle_name, 
            'suffix': self.suffix}
  as_dict = property(get_name_as_dict)
    
  