require(dplyr) |> suppressMessages()
require(igraph) |> suppressMessages()
require(sfnetworks) |> suppressMessages()
require(networkUtils) |> suppressMessages()

create_demo_graph = function() {
  g <- igraph::make_tree(20, 3, mode = "out")
  nV <- length(V(g))
  nE <- length(E(g))
  V(g)$label <- sample(letters, nV, replace = T)
  V(g)$attr1_int <- sample(seq(10), nV, replace = T)
  V(g)$attr2_letter <- sample(LETTERS, nV, replace = T)
  V(g)$attr3_numb <- runif(nV) * 100
  sp_df = data.frame(x = runif(nV), y= runif(nV)) |> 
    sf::st_as_sf(coords=c('x', 'y'))
  V(g)$attr4_geom <- sp_df$geom
  E(g)$attr1 <- runif(nE) * 100
  return(g)
}

g = create_demo_graph()
#V(g)$title <- pasteNodeDetails(g)

G = tidygraph::as_tbl_graph(g)
print(G)