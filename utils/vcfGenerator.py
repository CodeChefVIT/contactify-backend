import vobject

def generateVcard(row, headers, vCards):
    vcard = vobject.vCard()

    fn = row.get(headers.get("First Name","Not Found"),"")+row.get(headers.get("Last Name","Not Found"),"")
    if fn:
        vcard.add("fn").value = fn

    vcard.add("n").value = vobject.vcard.Name(
        family=row.get(headers.get("Last Name","Not Found"),""),
        given=row.get(headers.get("First Name","Not Found"),""),
        additional=row.get(headers.get("Middle Name","Not Found"),""),
        suffix=row.get(headers.get("Suffix","Not Found"),""),
        prefix=row.get(headers.get("Prefix","Not Found"),"")
    )

    phones = (row.get(headers.get("Phone Number","Not Found"),""))
    if phones:
        for phone in (row.get(headers.get("Phone Number","Not Found"),"")).split(","):
            telephone = vcard.add("tel")
            telephone.type_param = ["HOME"]
            telephone.value = phone
    
    vcard.add('version').value = '4.0'
    vCards.append(vcard.serialize())

def generateVcf(df, headers,split):
    vCards=[]
    df.apply(lambda row: generateVcard(row,headers,vCards),axis=1)
    if not split:
        vcardString = "\n".join(vCards)
        return vcardString
