
function killLeto(s)
    if s.text=="Leto" then
        return {pandoc.Strikeout(s.text)}
    end
end


function Div(e)
    local E = e
    if e.classes[1]=='twocol' then
      print('p div found')
      for i,j in pairs(e.content) do
        -- print(i,j)
        j = j:walk {
            Str = killLeto
        }
        e.content[i] = j -- this way you preserved layout
      end
    end
    return e
end

function BulletList(s)
    print(s.content[1])
end