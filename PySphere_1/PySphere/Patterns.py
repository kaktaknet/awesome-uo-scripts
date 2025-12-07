from __future__ import division
import string

#Ready these patterns.
def addVerA(compiler, ver):
	compiler.convert[ver]=[]
	compiler.convert[ver].append(('<?safe.','0<?'))
	
	compiler.supports[ver]={}
	compiler.supports[ver]['#']=1
	compiler.supports[ver]['<??>']=1
	compiler.supports[ver]['functionParameters']=1
	
	compiler.patterns[ver]={}
	compiler.patterns[ver]['finduid']={}
	compiler.patterns[ver]['finduid']['supported']=1
	compiler.patterns[ver]['finduid']['start']='finduid(%v).%c'
	compiler.patterns[ver]['finduid']['end']=None
	compiler.patterns[ver]['finduid']['body_external']=0
	compiler.patterns[ver]['finduid']['external_start']=None
	compiler.patterns[ver]['finduid']['external_end']=None
	
	compiler.patterns[ver]['local']={}
	compiler.patterns[ver]['local']['supported']=1
	compiler.patterns[ver]['local']['start']='ARG(%c)'
	compiler.patterns[ver]['local']['end']=None
	compiler.patterns[ver]['local']['body_external']=0
	compiler.patterns[ver]['local']['external_start']=None
	compiler.patterns[ver]['local']['external_end']=None
	
	compiler.patterns[ver]['localset']={}
	compiler.patterns[ver]['localset']['supported']=1
	compiler.patterns[ver]['localset']['start']='ARG(%c,%v)\n'
	compiler.patterns[ver]['localset']['end']=None
	compiler.patterns[ver]['localset']['body_external']=0
	compiler.patterns[ver]['localset']['external_start']=None
	compiler.patterns[ver]['localset']['external_end']=None
	
	compiler.patterns[ver+'readable']={}
	compiler.patterns[ver+'readable']['local']={}
	compiler.patterns[ver+'readable']['local']['supported']=1
	compiler.patterns[ver+'readable']['local']['start']='var.%c'
	compiler.patterns[ver+'readable']['local']['end']=None
	compiler.patterns[ver+'readable']['local']['body_external']=0
	compiler.patterns[ver+'readable']['local']['external_start']=None
	compiler.patterns[ver+'readable']['local']['external_end']=None
	
	compiler.patterns[ver+'readable']['localset']={}
	compiler.patterns[ver+'readable']['localset']['supported']=1
	compiler.patterns[ver+'readable']['localset']['start']='var.%c=%v\n'
	compiler.patterns[ver+'readable']['localset']['end']=None
	compiler.patterns[ver+'readable']['localset']['body_external']=0
	compiler.patterns[ver+'readable']['localset']['external_start']=None
	compiler.patterns[ver+'readable']['localset']['external_end']=None
	
	compiler.patterns[ver]['if']={}
	compiler.patterns[ver]['if']['supported']=1
	compiler.patterns[ver]['if']['start']='IF %c\n'
	compiler.patterns[ver]['if']['end']='ENDIF\n'
	compiler.patterns[ver]['if']['body_external']=0
	compiler.patterns[ver]['if']['external_start']=None
	compiler.patterns[ver]['if']['external_end']=None
	
	compiler.patterns[ver]['while']={}
	compiler.patterns[ver]['while']['supported']=1
	compiler.patterns[ver]['while']['start']='WHILE %c\n'
	compiler.patterns[ver]['while']['end']='ENDWHILE\n'
	compiler.patterns[ver]['while']['body_external']=0
	compiler.patterns[ver]['while']['external_start']=None
	compiler.patterns[ver]['while']['external_end']=None
	
	compiler.patterns[ver]['forrange']={}
	compiler.patterns[ver]['forrange']['supported']=1
	compiler.patterns[ver]['forrange']['start']='%<%v%>%),%i)\nWHILE (%v<%x)\n'
	compiler.patterns[ver]['forrange']['end']='%<%v%>%),#+%c)\nENDWHILE\n'
	compiler.patterns[ver]['forrange']['body_external']=0
	compiler.patterns[ver]['forrange']['external_start']=None
	compiler.patterns[ver]['forrange']['external_end']=None
	
	compiler.patterns[ver]['forrangerev']={}
	compiler.patterns[ver]['forrangerev']['supported']=1
	compiler.patterns[ver]['forrangerev']['start']='%<%v%>%),%i)\nWHILE (%v>%x)\n'
	compiler.patterns[ver]['forrangerev']['end']='%<%v%>%),#-%c)\nENDWHILE\n'
	compiler.patterns[ver]['forrangerev']['body_external']=0
	compiler.patterns[ver]['forrangerev']['external_start']=None
	compiler.patterns[ver]['forrangerev']['external_end']=None
	
	compiler.patterns[ver]['forarray']={}
	compiler.patterns[ver]['forarray']['supported']=1
	#compiler.patterns[ver]['forarray']['start']='%<%V%>%),0)\n%<%v%>%),%A)\nWHILE (%V<<?%<%a%>.GetCount?>)\n'
	compiler.patterns[ver]['forarray']['start']='%<%V%>%),0)\n%<%v%>%),%A)\nWHILE (strlen(%v))\n'
	
	compiler.patterns[ver]['forarray']['end']='%<%V%>%),#+1)\n%<%v%>%),%A)\nENDWHILE\n'
	compiler.patterns[ver]['forarray']['body_external']=0
	compiler.patterns[ver]['forarray']['external_start']=None
	compiler.patterns[ver]['forarray']['external_end']=None

	compiler.patterns[ver+'readable']['forrange']={}
	compiler.patterns[ver+'readable']['forrange']['supported']=1
	compiler.patterns[ver+'readable']['forrange']['start']='%<%v%>=%i\nWHILE (%v<%x)\n'
	compiler.patterns[ver+'readable']['forrange']['end']='%<%v%>=%v+%c\nENDWHILE\n'
	compiler.patterns[ver+'readable']['forrange']['body_external']=0
	compiler.patterns[ver+'readable']['forrange']['external_start']=None
	compiler.patterns[ver+'readable']['forrange']['external_end']=None
	
	compiler.patterns[ver+'readable']['forrangerev']={}
	compiler.patterns[ver+'readable']['forrangerev']['supported']=1
	compiler.patterns[ver+'readable']['forrangerev']['start']='%<%v%>=%i\nWHILE (%v>%x)\n'
	compiler.patterns[ver+'readable']['forrangerev']['end']='%<%v%>=%v-%c\nENDWHILE\n'
	compiler.patterns[ver+'readable']['forrangerev']['body_external']=0
	compiler.patterns[ver+'readable']['forrangerev']['external_start']=None
	compiler.patterns[ver+'readable']['forrangerev']['external_end']=None
	
	compiler.patterns[ver+'readable']['forarray']={}
	compiler.patterns[ver+'readable']['forarray']['supported']=1
	#compiler.patterns[ver+'readable']['forarray']['start']='%<%V%>=0\n%<%v%>=%A\nWHILE (%V<<?%<%a%>.GetCount?>)\n'
	compiler.patterns[ver+'readable']['forarray']['start']='%<%V%>=0\n%<%v%>=%A\nWHILE (strlen(%v))\n'
	compiler.patterns[ver+'readable']['forarray']['end']='%<%V%>=%V+1\n%<%v%>=%A\nENDWHILE\n'
	compiler.patterns[ver+'readable']['forarray']['body_external']=0
	compiler.patterns[ver+'readable']['forarray']['external_start']=None
	compiler.patterns[ver+'readable']['forarray']['external_end']=None

#Ready the patterns used for compiling to 99x scripts.
def add99x(compiler):
	compiler.convert['99x']=[]
	compiler.convert['99x'].append(('<safe.','0<'))
	
	compiler.supports['99x']={}
	compiler.supports['99x']['#']=1
	compiler.supports['99x']['<??>']=0
	compiler.supports['99x']['functionParameters']=1
	
	compiler.patterns['99x']={}
	compiler.patterns['99x']['finduid']={}
	compiler.patterns['99x']['finduid']['supported']=1
	compiler.patterns['99x']['finduid']['start']='finduid(%v).%c'
	compiler.patterns['99x']['finduid']['end']=None
	compiler.patterns['99x']['finduid']['body_external']=0
	compiler.patterns['99x']['finduid']['external_start']=None
	compiler.patterns['99x']['finduid']['external_end']=None
	
	compiler.patterns['99x']['local']={}
	compiler.patterns['99x']['local']['supported']=1
	compiler.patterns['99x']['local']['start']='ARG(%c)'
	compiler.patterns['99x']['local']['end']=None
	compiler.patterns['99x']['local']['body_external']=0
	compiler.patterns['99x']['local']['external_start']=None
	compiler.patterns['99x']['local']['external_end']=None
	
	compiler.patterns['99x']['localset']={}
	compiler.patterns['99x']['localset']['supported']=1
	compiler.patterns['99x']['localset']['start']='ARG(%c,%v)\n'
	compiler.patterns['99x']['localset']['end']=None
	compiler.patterns['99x']['localset']['body_external']=0
	compiler.patterns['99x']['localset']['external_start']=None
	compiler.patterns['99x']['localset']['external_end']=None
	
	compiler.patterns['99xreadable']={}
	compiler.patterns['99xreadable']['local']={}
	compiler.patterns['99xreadable']['local']['supported']=1
	compiler.patterns['99xreadable']['local']['start']='var.%c'
	compiler.patterns['99xreadable']['local']['end']=None
	compiler.patterns['99xreadable']['local']['body_external']=0
	compiler.patterns['99xreadable']['local']['external_start']=None
	compiler.patterns['99xreadable']['local']['external_end']=None
	
	compiler.patterns['99xreadable']['localset']={}
	compiler.patterns['99xreadable']['localset']['supported']=1
	compiler.patterns['99xreadable']['localset']['start']='var.%c=%v\n'
	compiler.patterns['99xreadable']['localset']['end']=None
	compiler.patterns['99xreadable']['localset']['body_external']=0
	compiler.patterns['99xreadable']['localset']['external_start']=None
	compiler.patterns['99xreadable']['localset']['external_end']=None
	
	compiler.patterns['99x']['if']={}
	compiler.patterns['99x']['if']['supported']=1
	compiler.patterns['99x']['if']['start']='IF %c\n'
	compiler.patterns['99x']['if']['end']='ENDIF\n'
	compiler.patterns['99x']['if']['body_external']=0
	compiler.patterns['99x']['if']['external_start']=None
	compiler.patterns['99x']['if']['external_end']=None
	
	compiler.patterns['99x']['while']={}
	compiler.patterns['99x']['while']['supported']=1
	compiler.patterns['99x']['while']['start']='WHILE %c\n'
	compiler.patterns['99x']['while']['end']='ENDWHILE\n'
	compiler.patterns['99x']['while']['body_external']=0
	compiler.patterns['99x']['while']['external_start']=None
	compiler.patterns['99x']['while']['external_end']=None
	
	compiler.patterns['99x']['forrange']={}
	compiler.patterns['99x']['forrange']['supported']=1
	compiler.patterns['99x']['forrange']['start']='%<%v%>%),%i)\nWHILE (%v<%x)\n'
	compiler.patterns['99x']['forrange']['end']='%<%v%>%),#+%c)\nENDWHILE\n'
	compiler.patterns['99x']['forrange']['body_external']=0
	compiler.patterns['99x']['forrange']['external_start']=None
	compiler.patterns['99x']['forrange']['external_end']=None
	
	compiler.patterns['99x']['forrangerev']={}
	compiler.patterns['99x']['forrangerev']['supported']=1
	compiler.patterns['99x']['forrangerev']['start']='%<%v%>%),%i)\nWHILE (%v>%x)\n'
	compiler.patterns['99x']['forrangerev']['end']='%<%v%>%),#-%c)\nENDWHILE\n'
	compiler.patterns['99x']['forrangerev']['body_external']=0
	compiler.patterns['99x']['forrangerev']['external_start']=None
	compiler.patterns['99x']['forrangerev']['external_end']=None
	
	compiler.patterns['99x']['forarray']={}
	compiler.patterns['99x']['forarray']['supported']=1
	compiler.patterns['99x']['forarray']['start']='%<%V%>%),0)\n%<%v%>%),%A)\nWHILE (%V<<%<%a%>.GetCount>)\n'
	compiler.patterns['99x']['forarray']['end']='%<%V%>%),#+1)\n%<%v%>%),%A)\nENDWHILE\n'
	compiler.patterns['99x']['forarray']['body_external']=0
	compiler.patterns['99x']['forarray']['external_start']=None
	compiler.patterns['99x']['forarray']['external_end']=None

	compiler.patterns['99xreadable']['forrange']={}
	compiler.patterns['99xreadable']['forrange']['supported']=1
	compiler.patterns['99xreadable']['forrange']['start']='%<%v%>=%i\nWHILE (%v<%x)\n'
	compiler.patterns['99xreadable']['forrange']['end']='%<%v%>=%v+%c\nENDWHILE\n'
	compiler.patterns['99xreadable']['forrange']['body_external']=0
	compiler.patterns['99xreadable']['forrange']['external_start']=None
	compiler.patterns['99xreadable']['forrange']['external_end']=None
	
	compiler.patterns['99xreadable']['forrangerev']={}
	compiler.patterns['99xreadable']['forrangerev']['supported']=1
	compiler.patterns['99xreadable']['forrangerev']['start']='%<%v%>=%i\nWHILE (%v>%x)\n'
	compiler.patterns['99xreadable']['forrangerev']['end']='%<%v%>=%v-%c\nENDWHILE\n'
	compiler.patterns['99xreadable']['forrangerev']['body_external']=0
	compiler.patterns['99xreadable']['forrangerev']['external_start']=None
	compiler.patterns['99xreadable']['forrangerev']['external_end']=None
	
	compiler.patterns['99xreadable']['forarray']={}
	compiler.patterns['99xreadable']['forarray']['supported']=1
	compiler.patterns['99xreadable']['forarray']['start']='%<%V%>=0\n%<%v%>=%A\nWHILE (%V<<%<%a%>.GetCount)\n'
	compiler.patterns['99xreadable']['forarray']['end']='%<%V%>=%V+1\n%<%v%>=%A\nENDWHILE\n'
	compiler.patterns['99xreadable']['forarray']['body_external']=0
	compiler.patterns['99xreadable']['forarray']['external_start']=None
	compiler.patterns['99xreadable']['forarray']['external_end']=None

#Ready the patterns used for compiling to 99w scripts.
def add99w(compiler):
	compiler.convert['99w']=[]
	compiler.convert['99w'].append(('<safe.','0<'))
	
	compiler.supports['99w']={}
	compiler.supports['99w']['#']=1
	compiler.supports['99w']['<??>']=0
	compiler.supports['99w']['functionParameters']=1
	
	compiler.patterns['99w']={}
	compiler.patterns['99w']['finduid']={}
	compiler.patterns['99w']['finduid']['supported']=1
	compiler.patterns['99w']['finduid']['start']='finduid(%v).%c'
	compiler.patterns['99w']['finduid']['end']=None
	compiler.patterns['99w']['finduid']['body_external']=0
	compiler.patterns['99w']['finduid']['external_start']=None
	compiler.patterns['99w']['finduid']['external_end']=None
	
	compiler.patterns['99w']['local']={}
	compiler.patterns['99w']['local']['supported']=1
	compiler.patterns['99w']['local']['start']='ARG(%c)'
	compiler.patterns['99w']['local']['end']=None
	compiler.patterns['99w']['local']['body_external']=0
	compiler.patterns['99w']['local']['external_start']=None
	compiler.patterns['99w']['local']['external_end']=None
	
	compiler.patterns['99w']['localset']={}
	compiler.patterns['99w']['localset']['supported']=1
	compiler.patterns['99w']['localset']['start']='ARG(%c,%v)\n'
	compiler.patterns['99w']['localset']['end']=None
	compiler.patterns['99w']['localset']['body_external']=0
	compiler.patterns['99w']['localset']['external_start']=None
	compiler.patterns['99w']['localset']['external_end']=None
	
	compiler.patterns['99xreadable']={}
	compiler.patterns['99xreadable']['local']={}
	compiler.patterns['99xreadable']['local']['supported']=1
	compiler.patterns['99xreadable']['local']['start']='var.%c'
	compiler.patterns['99xreadable']['local']['end']=None
	compiler.patterns['99xreadable']['local']['body_external']=0
	compiler.patterns['99xreadable']['local']['external_start']=None
	compiler.patterns['99xreadable']['local']['external_end']=None
	
	compiler.patterns['99xreadable']['localset']={}
	compiler.patterns['99xreadable']['localset']['supported']=1
	compiler.patterns['99xreadable']['localset']['start']='var.%c=%v\n'
	compiler.patterns['99xreadable']['localset']['end']=None
	compiler.patterns['99xreadable']['localset']['body_external']=0
	compiler.patterns['99xreadable']['localset']['external_start']=None
	compiler.patterns['99xreadable']['localset']['external_end']=None
	
	compiler.patterns['99w']['if']={}
	compiler.patterns['99w']['if']['supported']=1
	compiler.patterns['99w']['if']['start']='IF %c\n'
	compiler.patterns['99w']['if']['end']='ENDIF\n'
	compiler.patterns['99w']['if']['body_external']=0
	compiler.patterns['99w']['if']['external_start']=None
	compiler.patterns['99w']['if']['external_end']=None
	
	compiler.patterns['99w']['while']={}
	compiler.patterns['99w']['while']['supported']=1
	compiler.patterns['99w']['while']['start']='WHILE %c\n'
	compiler.patterns['99w']['while']['end']='ENDWHILE\n'
	compiler.patterns['99w']['while']['body_external']=0
	compiler.patterns['99w']['while']['external_start']=None
	compiler.patterns['99w']['while']['external_end']=None
	
	compiler.patterns['99w']['forrange']={}
	compiler.patterns['99w']['forrange']['supported']=1
	compiler.patterns['99w']['forrange']['start']='%<%v%>%),%i)\nWHILE (%v<%x)\n'
	compiler.patterns['99w']['forrange']['end']='%<%v%>%),#+%c)\nENDWHILE\n'
	compiler.patterns['99w']['forrange']['body_external']=0
	compiler.patterns['99w']['forrange']['external_start']=None
	compiler.patterns['99w']['forrange']['external_end']=None
	
	compiler.patterns['99w']['forrangerev']={}
	compiler.patterns['99w']['forrangerev']['supported']=1
	compiler.patterns['99w']['forrangerev']['start']='%<%v%>%),%i)\nWHILE (%v>%x)\n'
	compiler.patterns['99w']['forrangerev']['end']='%<%v%>%),#-%c)\nENDWHILE\n'
	compiler.patterns['99w']['forrangerev']['body_external']=0
	compiler.patterns['99w']['forrangerev']['external_start']=None
	compiler.patterns['99w']['forrangerev']['external_end']=None
	
	compiler.patterns['99w']['forarray']={}
	compiler.patterns['99w']['forarray']['supported']=1
	compiler.patterns['99w']['forarray']['start']='%<%V%>%),0)\n%<%v%>%),%A)\nWHILE (%V<<%<%a%>.GetCount>)\n'
	compiler.patterns['99w']['forarray']['end']='%<%V%>%),#+1)\n%<%v%>%),%A)\nENDWHILE\n'
	compiler.patterns['99w']['forarray']['body_external']=0
	compiler.patterns['99w']['forarray']['external_start']=None
	compiler.patterns['99w']['forarray']['external_end']=None

	compiler.patterns['99xreadable']['forrange']={}
	compiler.patterns['99xreadable']['forrange']['supported']=1
	compiler.patterns['99xreadable']['forrange']['start']='%<%v%>=%i\nWHILE (%v<%x)\n'
	compiler.patterns['99xreadable']['forrange']['end']='%<%v%>=%v+%c\nENDWHILE\n'
	compiler.patterns['99xreadable']['forrange']['body_external']=0
	compiler.patterns['99xreadable']['forrange']['external_start']=None
	compiler.patterns['99xreadable']['forrange']['external_end']=None
	
	compiler.patterns['99xreadable']['forrangerev']={}
	compiler.patterns['99xreadable']['forrangerev']['supported']=1
	compiler.patterns['99xreadable']['forrangerev']['start']='%<%v%>=%i\nWHILE (%v>%x)\n'
	compiler.patterns['99xreadable']['forrangerev']['end']='%<%v%>=%v-%c\nENDWHILE\n'
	compiler.patterns['99xreadable']['forrangerev']['body_external']=0
	compiler.patterns['99xreadable']['forrangerev']['external_start']=None
	compiler.patterns['99xreadable']['forrangerev']['external_end']=None
	
	compiler.patterns['99xreadable']['forarray']={}
	compiler.patterns['99xreadable']['forarray']['supported']=1
	compiler.patterns['99xreadable']['forarray']['start']='%<%V%>=0\n%<%v%>=%A\nWHILE (%V<<%<%a%>.GetCount)\n'
	compiler.patterns['99xreadable']['forarray']['end']='%<%V%>=%V+1\n%<%v%>=%A\nENDWHILE\n'
	compiler.patterns['99xreadable']['forarray']['body_external']=0
	compiler.patterns['99xreadable']['forarray']['external_start']=None
	compiler.patterns['99xreadable']['forarray']['external_end']=None

#Ready the patterns used for compiling to 99v scripts.
def add99v(compiler):
	compiler.convert['99v']=[]
	
	compiler.supports['99v']={}
	compiler.supports['99v']['#']=0
	compiler.supports['99v']['<??>']=0
	compiler.supports['99v']['functionParameters']=1
	
	compiler.patterns['99v']={}
	compiler.patterns['99v']['finduid']={}
	compiler.patterns['99v']['finduid']['supported']=1
	compiler.patterns['99v']['finduid']['start']='finduid(%v).%c'
	compiler.patterns['99v']['finduid']['end']=None
	compiler.patterns['99v']['finduid']['body_external']=0
	compiler.patterns['99v']['finduid']['external_start']=None
	compiler.patterns['99v']['finduid']['external_end']=None
	
	compiler.patterns['99v']['local']={}
	compiler.patterns['99v']['local']['supported']=1
	compiler.patterns['99v']['local']['start']='var.py__%m__%f__%c'
	compiler.patterns['99v']['local']['end']=None
	compiler.patterns['99v']['local']['body_external']=0
	compiler.patterns['99v']['local']['external_start']=None
	compiler.patterns['99v']['local']['external_end']=None
	
	compiler.patterns['99v']['localset']={}
	compiler.patterns['99v']['localset']['supported']=1
	compiler.patterns['99v']['localset']['start']='var.py__%m__%f__%c=%v\n'
	compiler.patterns['99v']['localset']['end']=None
	compiler.patterns['99v']['localset']['body_external']=0
	compiler.patterns['99v']['localset']['external_start']=None
	compiler.patterns['99v']['localset']['external_end']=None
	
	compiler.patterns['99ureadable']={}
	compiler.patterns['99ureadable']['local']={}
	compiler.patterns['99ureadable']['local']['supported']=1
	compiler.patterns['99ureadable']['local']['start']='var.%c'
	compiler.patterns['99ureadable']['local']['end']=None
	compiler.patterns['99ureadable']['local']['body_external']=0
	compiler.patterns['99ureadable']['local']['external_start']=None
	compiler.patterns['99ureadable']['local']['external_end']=None
	
	compiler.patterns['99ureadable']['localset']={}
	compiler.patterns['99ureadable']['localset']['supported']=1
	compiler.patterns['99ureadable']['localset']['start']='var.%c=%v\n'
	compiler.patterns['99ureadable']['localset']['end']=None
	compiler.patterns['99ureadable']['localset']['body_external']=0
	compiler.patterns['99ureadable']['localset']['external_start']=None
	compiler.patterns['99ureadable']['localset']['external_end']=None
	
	compiler.patterns['99v']['if']={}
	compiler.patterns['99v']['if']['supported']=1
	compiler.patterns['99v']['if']['start']='IF %c\n'
	compiler.patterns['99v']['if']['end']='ENDIF\n'
	compiler.patterns['99v']['if']['body_external']=0
	compiler.patterns['99v']['if']['external_start']=None
	compiler.patterns['99v']['if']['external_end']=None
	
	compiler.patterns['99v']['while']={}
	compiler.patterns['99v']['while']['supported']=1
	compiler.patterns['99v']['while']['start']='WHILE %c\n'
	compiler.patterns['99v']['while']['end']='ENDWHILE\n'
	compiler.patterns['99v']['while']['body_external']=0
	compiler.patterns['99v']['while']['external_start']=None
	compiler.patterns['99v']['while']['external_end']=None
	
	compiler.patterns['99v']['forrange']={}
	compiler.patterns['99v']['forrange']['supported']=1
	compiler.patterns['99v']['forrange']['start']='%<%v%>=%i\nWHILE (%v<%x)\n'
	compiler.patterns['99v']['forrange']['end']='%<%v%>=%v+%c\nENDWHILE\n'
	compiler.patterns['99v']['forrange']['body_external']=0
	compiler.patterns['99v']['forrange']['external_start']=None
	compiler.patterns['99v']['forrange']['external_end']=None
	
	compiler.patterns['99v']['forrangerev']={}
	compiler.patterns['99v']['forrangerev']['supported']=1
	compiler.patterns['99v']['forrangerev']['start']='%<%v%>=%i\nWHILE (%v>%x)\n'
	compiler.patterns['99v']['forrangerev']['end']='%<%v%>=%v-%c\nENDWHILE\n'
	compiler.patterns['99v']['forrangerev']['body_external']=0
	compiler.patterns['99v']['forrangerev']['external_start']=None
	compiler.patterns['99v']['forrangerev']['external_end']=None
	
	compiler.patterns['99v']['forarray']={}
	compiler.patterns['99v']['forarray']['supported']=1
	compiler.patterns['99v']['forarray']['start']='%<%V%>=0\n%<%v%>=%A\nWHILE (strlen(%v))\n'
	compiler.patterns['99v']['forarray']['end']='%<%V%>=%V+1\n%<%v%>=%A\nENDWHILE\n'
	compiler.patterns['99v']['forarray']['body_external']=0
	compiler.patterns['99v']['forarray']['external_start']=None
	compiler.patterns['99v']['forarray']['external_end']=None
	
#Ready the patterns used for compiling to 99u scripts.
def add99u(compiler):
	compiler.convert['99u']=[]
	
	compiler.supports['99u']={}
	compiler.supports['99u']['#']=0
	compiler.supports['99u']['<??>']=0
	compiler.supports['99u']['functionParameters']=1
	
	compiler.patterns['99u']={}
	compiler.patterns['99u']['finduid']={}
	compiler.patterns['99u']['finduid']['supported']=1
	compiler.patterns['99u']['finduid']['start']='finduid(%v).%c'
	compiler.patterns['99u']['finduid']['end']=None
	compiler.patterns['99u']['finduid']['body_external']=0
	compiler.patterns['99u']['finduid']['external_start']=None
	compiler.patterns['99u']['finduid']['external_end']=None
	
	compiler.patterns['99u']['local']={}
	compiler.patterns['99u']['local']['supported']=1
	compiler.patterns['99u']['local']['start']='var.py__%m__%f__%c'
	compiler.patterns['99u']['local']['end']=None
	compiler.patterns['99u']['local']['body_external']=0
	compiler.patterns['99u']['local']['external_start']=None
	compiler.patterns['99u']['local']['external_end']=None
	
	compiler.patterns['99u']['localset']={}
	compiler.patterns['99u']['localset']['supported']=1
	compiler.patterns['99u']['localset']['start']='var.py__%m__%f__%c=%v\n'
	compiler.patterns['99u']['localset']['end']=None
	compiler.patterns['99u']['localset']['body_external']=0
	compiler.patterns['99u']['localset']['external_start']=None
	compiler.patterns['99u']['localset']['external_end']=None
	
	compiler.patterns['99ureadable']={}
	compiler.patterns['99ureadable']['local']={}
	compiler.patterns['99ureadable']['local']['supported']=1
	compiler.patterns['99ureadable']['local']['start']='var.%c'
	compiler.patterns['99ureadable']['local']['end']=None
	compiler.patterns['99ureadable']['local']['body_external']=0
	compiler.patterns['99ureadable']['local']['external_start']=None
	compiler.patterns['99ureadable']['local']['external_end']=None
	
	compiler.patterns['99ureadable']['localset']={}
	compiler.patterns['99ureadable']['localset']['supported']=1
	compiler.patterns['99ureadable']['localset']['start']='var.%c=%v\n'
	compiler.patterns['99ureadable']['localset']['end']=None
	compiler.patterns['99ureadable']['localset']['body_external']=0
	compiler.patterns['99ureadable']['localset']['external_start']=None
	compiler.patterns['99ureadable']['localset']['external_end']=None
	
	compiler.patterns['99u']['if']={}
	compiler.patterns['99u']['if']['supported']=1
	compiler.patterns['99u']['if']['start']='IF %c\n'
	compiler.patterns['99u']['if']['end']='ENDIF\n'
	compiler.patterns['99u']['if']['body_external']=0
	compiler.patterns['99u']['if']['external_start']=None
	compiler.patterns['99u']['if']['external_end']=None
	
	compiler.patterns['99u']['while']={}
	compiler.patterns['99u']['while']['supported']=1
	compiler.patterns['99u']['while']['start']='WHILE %c\n'
	compiler.patterns['99u']['while']['end']='ENDWHILE\n'
	compiler.patterns['99u']['while']['body_external']=0
	compiler.patterns['99u']['while']['external_start']=None
	compiler.patterns['99u']['while']['external_end']=None
	
	compiler.patterns['99u']['forrange']={}
	compiler.patterns['99u']['forrange']['supported']=1
	compiler.patterns['99u']['forrange']['start']='%<%v%>=%i\nWHILE (%v<%x)\n'
	compiler.patterns['99u']['forrange']['end']='%<%v%>=%v+%c\nENDWHILE\n'
	compiler.patterns['99u']['forrange']['body_external']=0
	compiler.patterns['99u']['forrange']['external_start']=None
	compiler.patterns['99u']['forrange']['external_end']=None
	
	compiler.patterns['99u']['forrangerev']={}
	compiler.patterns['99u']['forrangerev']['supported']=1
	compiler.patterns['99u']['forrangerev']['start']='%<%v%>=%i\nWHILE (%v>%x)\n'
	compiler.patterns['99u']['forrangerev']['end']='%<%v%>=%v-%c\nENDWHILE\n'
	compiler.patterns['99u']['forrangerev']['body_external']=0
	compiler.patterns['99u']['forrangerev']['external_start']=None
	compiler.patterns['99u']['forrangerev']['external_end']=None
	
	compiler.patterns['99u']['forarray']={}
	compiler.patterns['99u']['forarray']['supported']=1
	compiler.patterns['99u']['forarray']['start']='%<%V%>=0\n%<%v%>=%A\nWHILE (strlen(%v))\n'
	compiler.patterns['99u']['forarray']['end']='%<%V%>=%V+1\n%<%v%>=%A\nENDWHILE\n'
	compiler.patterns['99u']['forarray']['body_external']=0
	compiler.patterns['99u']['forarray']['external_start']=None
	compiler.patterns['99u']['forarray']['external_end']=None
	
#Ready the patterns used for compiling to 55i scripts.
def add55i(compiler):
	compiler.convert['55i']=[]
	compiler.convert['55i'].append(('finduid ','uid.'))
	compiler.convert['55i'].append(('[defnames ','[defname '))
	compiler.convert['55i'].append(('on=@userstats','on=@stats'))
	compiler.convert['55i'].append(('on=@userclick','on=@click'))
	compiler.convert['55i'].append(('on=@userdclick','on=@dclick'))
	compiler.convert['55i'].append(('on=@userprofile','on=@profile'))
	compiler.convert['55i'].append(('on=@userskills','on=@skills'))
	compiler.convert['55i'].append(('on=@itemuserclick','on=@itemclick'))
	compiler.convert['55i'].append(('on=@itemuserdclick','on=@itemdclick'))
	compiler.convert['55i'].append(('<safe.','0<'))
	
	compiler.supports['55i']={}
	compiler.supports['55i']['#']=0
	compiler.supports['55i']['<??>']=0
	compiler.supports['55i']['functionParameters']=0
	
	compiler.patterns['55i']={}
	compiler.patterns['55i']['finduid']={}
	compiler.patterns['55i']['finduid']['supported']=1
	compiler.patterns['55i']['finduid']['start']='uid.%-%<%v%>.%c'
	compiler.patterns['55i']['finduid']['end']=None
	compiler.patterns['55i']['finduid']['body_external']=0
	compiler.patterns['55i']['finduid']['external_start']=None
	compiler.patterns['55i']['finduid']['external_end']=None
	
	compiler.patterns['55i']['local']={}
	compiler.patterns['55i']['local']['supported']=1
	compiler.patterns['55i']['local']['start']='var.py__%m__%f__%c'
	compiler.patterns['55i']['local']['end']=None
	compiler.patterns['55i']['local']['body_external']=0
	compiler.patterns['55i']['local']['external_start']=None
	compiler.patterns['55i']['local']['external_end']=None
	
	compiler.patterns['55i']['localset']={}
	compiler.patterns['55i']['localset']['supported']=1
	compiler.patterns['55i']['localset']['start']='var.py__%m__%f__%c=%v\n'
	compiler.patterns['55i']['localset']['end']=None
	compiler.patterns['55i']['localset']['body_external']=0
	compiler.patterns['55i']['localset']['external_start']=None
	compiler.patterns['55i']['localset']['external_end']=None
	
	compiler.patterns['55ireadable']={}
	compiler.patterns['55ireadable']['local']={}
	compiler.patterns['55ireadable']['local']['supported']=1
	compiler.patterns['55ireadable']['local']['start']='var.%c'
	compiler.patterns['55ireadable']['local']['end']=None
	compiler.patterns['55ireadable']['local']['body_external']=0
	compiler.patterns['55ireadable']['local']['external_start']=None
	compiler.patterns['55ireadable']['local']['external_end']=None
	
	compiler.patterns['55ireadable']['localset']={}
	compiler.patterns['55ireadable']['localset']['supported']=1
	compiler.patterns['55ireadable']['localset']['start']='var.%c=%v\n'
	compiler.patterns['55ireadable']['localset']['end']=None
	compiler.patterns['55ireadable']['localset']['body_external']=0
	compiler.patterns['55ireadable']['localset']['external_start']=None
	compiler.patterns['55ireadable']['localset']['external_end']=None
	
	compiler.patterns['55i']['if']={}
	compiler.patterns['55i']['if']['supported']=1
	compiler.patterns['55i']['if']['start']='IF %c\n'
	compiler.patterns['55i']['if']['end']='ENDIF\n'
	compiler.patterns['55i']['if']['body_external']=0
	compiler.patterns['55i']['if']['external_start']=None
	compiler.patterns['55i']['if']['external_end']=None
	
	compiler.patterns['55i']['while']={}
	compiler.patterns['55i']['while']['supported']=1
	compiler.patterns['55i']['while']['start']='f_while_loop_%m_%f_%l\n'
	compiler.patterns['55i']['while']['end']=None
	compiler.patterns['55i']['while']['body_external']=1
	compiler.patterns['55i']['while']['external_start']='[function f_while_loop_%m_%f_%l]\nif !%c\nreturn\nendif\n'
	compiler.patterns['55i']['while']['external_end']='f_while_loop_%m_%f_%l\n'
	
	compiler.patterns['55i']['forrange']={}
	compiler.patterns['55i']['forrange']['supported']=1
	compiler.patterns['55i']['forrange']['start']='%<%v%>=%i\nfor_range_%m_%f_%l\n'
	compiler.patterns['55i']['forrange']['end']=None
	compiler.patterns['55i']['forrange']['body_external']=1
	compiler.patterns['55i']['forrange']['external_start']='[function f_for_range_%m_%f_%l]\nif %v>=%x\nreturn\nendif\n'
	compiler.patterns['55i']['forrange']['external_end']='%<%v%>=%v+%c\nf_for_range_%m_%f_%l\n'
	
	compiler.patterns['55i']['forrangerev']={}
	compiler.patterns['55i']['forrangerev']['supported']=1
	compiler.patterns['55i']['forrangerev']['start']='%<%v%>=%i\nfor_range_%m_%f_%l\n'
	compiler.patterns['55i']['forrangerev']['end']=None
	compiler.patterns['55i']['forrangerev']['body_external']=1
	compiler.patterns['55i']['forrangerev']['external_start']='[function f_for_range_%m_%f_%l]\nif %v<=%x\nreturn\nendif\n'
	compiler.patterns['55i']['forrangerev']['external_end']='%<%v%>=%v-%c\nf_for_range_%m_%f_%l\n'
	
	compiler.patterns['55i']['forarray']={}
	compiler.patterns['55i']['forarray']['supported']=1
	compiler.patterns['55i']['forarray']['start']='%<%V%>=0\n%<%v%>=%A\nf_for_array_%m_%f_%l\n'
	compiler.patterns['55i']['forarray']['end']=None
	compiler.patterns['55i']['forarray']['body_external']=1
	compiler.patterns['55i']['forarray']['external_start']='[function f_for_array_%m_%f_%l]\nif (!(strlen(%v)))\nreturn\nendif\n'
	compiler.patterns['55i']['forarray']['external_end']='%<%V%>=%V+1\n%<%v%>=%A\nf_for_array_%m_%f_%l\n'
