# -*- coding: utf-8 -*-

class Name:

  SALUTATIONS = ['MR','MS','MRS','DR','MISS','DOCTOR','CORP','SGT','PVT','JUDGE',
                 'CAPT','COL','MAJ','LT','LIEUTENANT','PRM','PATROLMAN','HON',
                 'OFFICER','REV','PRES','PRESIDENT',
                 'GOV','GOVERNOR','VICE PRESIDENT','VP','MAYOR','SIR','MADAM','HONERABLE']
  GENERATIONS = ['JR','SR','I','II','III','IV','V','VI','VII','VIII','IX','X',
                 '1ST','2ND','3RD','4TH','5TH','6TH','7TH','8TH','9TH','10TH',
                 'FIRST','SECOND','THIRD','FOURTH','FIFTH','SIXTH','SEVENTH',
                 'EIGHTH','NINTH','TENTH']
  SUFFIXES    = ['ESQ','PHD','MD']
  LNPREFIXES  = ['DE', 'DA', 'DI','LA', 'DU', 'DEL', 'DEI', 'VDA', 'DELLO', 'DELLA',
                 'DEGLI', 'DELLE', 'VAN', 'VON', 'DER', 'DEN', 'HEER', 'TEN', 'TER',
                 'VANDE', 'VANDEN', 'VANDER', 'VOOR', 'VER', 'AAN', 'MC', 'BEN','SAN',
                 'SAINZ','BIN','LI','LE','DES','AM','AUS\'M','VOM','ZUM','ZUR','TEN', 'IBN']
  NON_NAME    = ['A.K.A.','AKA','A/K/A','F.K.A','FKA','F/K/A','N/K/A','FICTITIOUS']
  CORP_ENTITY = ['NA','CORP','CO','INC','ASSOCIATES','SERVICE','LLC','LLP','PARTNERS',
                 'R/A','C/O', 'COUNTY','STATE',
                 'BANK','GROUP','MUTUAL','FARGO']
  SUPPLEMENTAL_INFO = ['WIFE OF','HUSBAND OF','SON OF','DAUGHTER OF']

  def get_has_non_name_values(self):
    for part in self.__split_name:
      if part.upper() in self.NON_NAME:
        return True
    return False
  has_non_name_values = property(get_has_non_name_values)

  def split_on_non_name(self):
    for part in self.__split_name:
      if part.upper() in self.NON_NAME:
        return self.__full_name.split(part)[0]

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

  def get_looks_corporate(self):
    if not self.__processed:
      self.__clean()
    for part in self.__split_name:
      if part.upper() in self.CORP_ENTITY:
        return True
    return False
  looks_corporate = property(get_looks_corporate)

  def get_has_suffix(self):
    if self.__split_name[-1].upper() in self.SUFFIXES:
      return True
    return False
  has_suffix = property(get_has_suffix)

  def get_has_generation(self):
    if not self.__processed:
      self.__clean()
    index = 0
    for part in self.__split_name:
      if part.upper() in self.GENERATIONS:
        if part == self.__split_name[-1]:
          return True
        if self.__split_name[index + 1].upper() not in self.SUFFIXES:
          index += 1
          continue
        else:
          return True
      index += 1
    return False
  has_generation = property(get_has_generation)

  def __clean(self):
    if self.has_non_name_values:
      self.__full_name = self.split_on_non_name()
    # last name, first style
    comma_index = self.__full_name.find(",")
    comma_index_value = None
    if comma_index > -1:
      comma_index_value = self.__full_name[:comma_index]
      if comma_index_value.upper() in self.SALUTATIONS:
        comma_index_value = None

    for supplemental_text in self.SUPPLEMENTAL_INFO:
      supplemental_index = self.__full_name.upper().find(supplemental_text)
      if supplemental_index > -1:
        self.__full_name = self.__full_name[0:supplemental_index].strip()

    unwanted = ['.',',','/','the']

    for char in unwanted:
      self.__full_name = self.__full_name.replace(char,'')
    self.__split_name = self.__full_name.split(" ")
    index = 0
    for part in self.__split_name:
      # remove lengthless items
      if len(part) == 0:
        del self.__split_name[index]
        continue
      # remove excess spaces from the beginning and end of items
      self.__split_name[index] = part.strip(" ")
      index += 1
    if self.__split_name[0] == comma_index_value:
      slot_it = True
      index = -1
      while slot_it:
        item_at_index = self.__split_name[index].upper()
        if item_at_index in self.GENERATIONS or \
           item_at_index in self.SUFFIXES:
          index -= 1
        else:
          insert_index = index + 1
          if insert_index == 0:
            insert_index = len(self.__split_name)
          self.__split_name.insert(insert_index, self.__split_name[0])
          del self.__split_name[0]
          slot_it = False
      self.__full_name = " ".join(self.__split_name)


  def __repr__(self):
    return unicode("<Name: '%s'>" % self.__full_name)

  def process_name(self):
    if self.__processed or self.looks_corporate:
      return

    self.__clean()

    name_parts = self.__split_name

    # Find salutation, save it, remove it
    if self.has_salutation:
      self.__salutation = name_parts[0]
      del name_parts[0]

    # Find generation, save it, remove it
    if self.has_generation:
      index = 0
      for part in name_parts:
        if part.upper() in self.GENERATIONS:
          if part == name_parts[-1]:
            self.__generation = part
            del name_parts[index]
            break
          store_generation = True
          if name_parts[index + 1].upper() not in self.SUFFIXES:
            store_generation = False
          if store_generation:
            self.__generation = part
            del name_parts[index]
        index += 1

    # Find suffix (or suffixes), save it, remove it
    if self.has_suffix:
      suffixes = []
      suffix_present = True
      while suffix_present:
        if name_parts[-1].upper() in self.SUFFIXES:
          suffixes.insert(0,name_parts[-1])
          del name_parts[-1]
        else:
          suffix_present = False
      self.__suffix = ", ".join(suffixes)


    # Save first name, remove it
    self.__first_name = name_parts[0]
    del name_parts[0]

    # The rest...
    if len(name_parts) > 1 and \
       name_parts[0].upper() not in self.LNPREFIXES:
      self.__middle_name = name_parts[0]
      del name_parts[0]
      if len(name_parts) > 1:
        mult_middle = True
        while mult_middle:
          if name_parts[0].upper() in self.LNPREFIXES or \
             len(name_parts) == 1:
            mult_middle = False
          else:
            self.__middle_name += " %s" % name_parts[0]
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
    self.__generation   = None
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

  def get_generation(self):
    return self.__generation
  generation = property(get_generation)

  def get_suffix(self):
    return self.__suffix
  suffix = property(get_suffix)

  def get_name_as_dict(self):
    return {'salutation': self.salutation,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'middle_name': self.middle_name,
            'generation' : self.generation,
            'suffix': self.suffix}
  as_dict = property(get_name_as_dict)
