//Original Bags By Dupre THANX!! *Ingot Bags*
//Edited to these Potion Bags For Full Sets In My Shard Dark Saints By Theron Of SOJ
using System; 
using Server; 
using Server.Items;

namespace Server.Items 
{ 
	public class StamBag : Bag 
	{ 
		[Constructable] 
		public StamBag() : this( 1 ) 
		{ 
		} 

		[Constructable] 
		public StamBag(int amount) 
		{ 
			Name = "StamBag";
			Hue = 1266;

			DropItem( new TotalRefreshPotion()); 
			DropItem( new TotalRefreshPotion()); 
			DropItem( new TotalRefreshPotion()); 
			DropItem( new TotalRefreshPotion()); 
			DropItem( new TotalRefreshPotion()); 
			DropItem( new TotalRefreshPotion()); 
			DropItem( new TotalRefreshPotion()); 
			DropItem( new TotalRefreshPotion()); 
			DropItem( new TotalRefreshPotion()); 
			DropItem( new TotalRefreshPotion()); 
                        
                           
			



       
		} 

		public StamBag( Serial serial ) : base( serial ) 
		{ 
		} 

		public override void Serialize( GenericWriter writer ) 
		{ 
			base.Serialize( writer ); 

			writer.Write( (int) 0 ); // version 
		} 

		public override void Deserialize( GenericReader reader ) 
		{ 
			base.Deserialize( reader ); 

			int version = reader.ReadInt(); 
		} 
	} 
} 
