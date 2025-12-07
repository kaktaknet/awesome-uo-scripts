To install this, please replace the following items in SPHEREITEMb2.scp....
Then resync...
ALSO... make sure you replace your sphereitem_multis.scp, housemenu.scp and add housegumps.scp

*Note, if you do not wish to replace sphereitem_multis, add these to every house multi in there.

ON=@TARGON_ITEM
HOUSE_TargonITEM
RETURN 1

ON=@TARGON_CHAR
HOUSE_TARGONCHAR
RETURN 1

**************

[ITEMDEF 0bd1]
DEFNAME=i_sign_brass
TYPE=T_SIGN_GUMP
DUPELIST=0bd0,0bcf,0bd1,0ba4,0ba6,0ba8,0baa,0bac,0bae,0bb0,0bb2,0bb4,0bb6,0bb8,0bba,0bbc,0bbe,0bc0,0bc2,0bc4,0bc6,0bc8,0bca,0bcc,0bce,0bd0,0bd2,0bd4,0bd6,0bd8,0bda,0bdc,0bde,0be0,0be2,0be4,0be6,0be8,0bea,0bec,0bee,0bf0,0bf2,0bf4,0bf6,0bf8,0bfa,0bfc,0bfe,0c00,0c02,0c04,0c06,0c08,0c0a,0c0c

CATEGORY=Decoration - Signs
SUBSECTION=Blank
DESCRIPTION=Brass Blank

ON=@DClick
IF !(<LINK> = 04fffffff)
House_init Coowner
House_init Biowner
LINK.LINK=<UID>
IF (<EVAL <SRC.UID>>==<LINK.MORE>)
DIALOG D_HOUSESIGN_OWNER
RETURN 1
ELSE
DIALOG D_HOUSE_NONOWNER
RETURN 1
ENDIF
ELSE
MESSAGE <NAME>
RETURN 1
ENDIF

[ITEMDEF 0bd2]
//brass sign
DEFNAME=i_sign_brass_2
TYPE=T_SIGN_GUMP
DUPELIST=0bd0,0bcf,0bd1,0ba4,0ba6,0ba8,0baa,0bac,0bae,0bb0,0bb2,0bb4,0bb6,0bb8,0bba,0bbc,0bbe,0bc0,0bc2,0bc4,0bc6,0bc8,0bca,0bcc,0bce,0bd0,0bd2,0bd4,0bd6,0bd8,0bda,0bdc,0bde,0be0,0be2,0be4,0be6,0be8,0bea,0bec,0bee,0bf0,0bf2,0bf4,0bf6,0bf8,0bfa,0bfc,0bfe,0c00,0c02,0c04,0c06,0c08,0c0a,0c0c

CATEGORY=Decoration - Signs
SUBSECTION=Blank
DESCRIPTION=Brass Blank

ON=@DClick
IF !(<LINK> = 04fffffff)
House_init Coowner
House_init Biowner
LINK.LINK=<UID>
IF (<EVAL <SRC.UID>>==<LINK.MORE>)
DIALOG D_HOUSESIGN_OWNER
RETURN 1
ELSE
DIALOG D_HOUSE_NONOWNER
RETURN 1
ENDIF
ELSE
MESSAGE <NAME>
RETURN 1
ENDIF
