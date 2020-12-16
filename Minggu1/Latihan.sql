-- select * from albums inner join artists on albums.ArtistId = artists.ArtistId where artists.ArtistId=3 or artists.ArtistId =1

-- select albums.Title ,artists.Name 
-- from albums,artists
-- inner join artists 
-- on albums.ArtistId = artists.ArtistId 
-- where artists.ArtistId=3 or (artists.ArtistId =1 and albums.Title = "Let There Be Rock");


-- select albums.Title ,artists.Name, tracks.Name
-- from albums,artists,tracks
-- inner join artists 
-- on albums.AlbumsId = tracks.AlbumsId 
-- where  artists.Name="Aerosmith" or (artists.Name ="AC/DC" and albums.Title = "Let There Be Rock")
-- order by artists.Name DESC


-- select * 
-- from albums 
-- inner join artists 
-- on albums.ArtistId = artists.ArtistId
-- where  artists.Name="Aerosmith" or (artists.Name ="AC/DC" and albums.Title = "Let There Be Rock")

-- select Name,Title  
-- from albums 
-- inner join artists 
-- on albums.ArtistId = artists.ArtistId
-- where  artists.Name="Aerosmith" or (artists.Name ="AC/DC" and albums.Title = "Let There Be Rock")


SELECT * FROM invoices WHERE InvoiceDate BETWEEN '2009-02-01 00:00:00' AND '2009-06-31 00:00:00';