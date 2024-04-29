
-- Reformat all heading text 
function Header(el)
  el.content = pandoc.Emph(el.content)
  quarto.log.output('Function Header is Eveluated..')
  print('Header.el.content is',el.content)
  print('Header type is', type(el.content))
  return el
end



function Div(blocks)
  -- for key, value in pairs(blocks) do
  --   print(key, value)
  -- end
  if blocks.classes[1] == 'twocol' then
    print("In div.twocol")
  --   pandoc.walk_block(blocks.content,{
  --     function(el) 
  --       pandoc.Emph(el)
  --     end
  --   })
  --   return blocks
  end
end



return {
  {
    Str = function (elem)
      if elem.text == "{{helloworld}}" then
        return pandoc.Emph {pandoc.Str "Hello, World"}
      else
        return elem
      end
    end,
  }
}






