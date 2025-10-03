import sys,os,re

from blues_lib.command.hook.processor.prev.AbsPrevProc import AbsPrevProc
from blues_lib.ai.prompt.AIPrompt import AIPrompt
from blues_lib.util.NestedDataReader import NestedDataReader
from blues_lib.util.NestedDataWriter import NestedDataWriter

class TextToAIQuery(AbsPrevProc):
  
  def execute(self)->bool:
    '''
    @description: Convert the text to ai query, change the bizdata and refresh the Model
    @return: None
    '''
    prompt = self._proc_conf.get('prompt')
    source = self._proc_conf.get('source',{})
    
    # must be a basic command
    target_data = source_data = self._input.bizdata
    target_path = source_path = source.get('path')

    if prompt and target_data and target_path:

      # update the source node data
      text = NestedDataReader.read_by_path(source_data,source_path)
      value = AIPrompt(prompt,text).get()
      # rewrite the source node data
      if has_written := NestedDataWriter.write_by_path(target_data,target_path,value):
        self._input.refresh()
      return has_written

    return False

  def _fail(self):
    self._output.message = f'mat_paras is not a list, data: {self._output.data}'
    self._output.code = 500
    self._output.data = ''

  def _join(self,paras:list[dict])->str:
    text = ''
    for para in paras:
      if para.get('type') == 'text':
        text += para.get('value')
    return text
