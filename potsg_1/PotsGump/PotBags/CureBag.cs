//Original Bags By Dupre THANX!! *Ingot Bags*
//Edited to these Potion Bags For Full Sets In My Shard Dark Saints By Theron Of SOJ
using System; 
using Server; 
using Server.Items;

namespace Server.Items 
{ 
	public class CureBag : Bag 
	{ 
		[Constructable] 
		public CureBag() : this( 1 ) 
		{ 
		} 

		[Constructable] 
		public CureBag(int amount) 
		{ 
			Name = "CureBag";
			Hue = 1260;

			DropItem( new GreaterCurePotion()); 
			DropItem( new GreaterCurePotion()); 
			DropItem( new GreaterCurePotion()); 
			DropItem( new GreaterCurePotion()); 
			DropItem( new GreaterCurePotion()); 
			DropItem( new GreaterCurePotion()); 
			DropItem( new GreaterCurePotion()); 
			DropItem( new GreaterCurePotion()); 
			DropItem( new GreaterCurePotion()); 
			DropItem( new GreaterCurePotion()); 
                        
                           
			



       
		} 

		public CureBag( Serial serial ) : base( serial ) 
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
