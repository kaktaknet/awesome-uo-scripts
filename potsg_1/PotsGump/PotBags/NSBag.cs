//Original Bags By Dupre THANX!! *Ingot Bags*
//Edited to these Potion Bags For Full Sets In My Shard Dark Saints By Theron Of SOJ
using System; 
using Server; 
using Server.Items;

namespace Server.Items 
{ 
	public class NSBag : Bag 
	{ 
		[Constructable] 
		public NSBag() : this( 1 ) 
		{ 
		} 

		[Constructable] 
		public NSBag(int amount) 
		{ 
			Name = "NSBag";
			Hue = 1150;

			DropItem( new NightSightPotion()); 
			DropItem( new NightSightPotion()); 
			DropItem( new NightSightPotion()); 
			DropItem( new NightSightPotion()); 
			DropItem( new NightSightPotion()); 
			DropItem( new NightSightPotion()); 
			DropItem( new NightSightPotion()); 
			DropItem( new NightSightPotion()); 
			DropItem( new NightSightPotion()); 
			DropItem( new NightSightPotion()); 
                        
                           
			



       
		} 

		public NSBag( Serial serial ) : base( serial ) 
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
