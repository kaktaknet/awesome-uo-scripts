//Original Bags By Dupre THANX!! *Ingot Bags*
//Edited to these Potion Bags For Full Sets In My Shard Dark Saints By Theron Of SOJ
using System; 
using Server; 
using Server.Items;

namespace Server.Items 
{ 
	public class HealBag : Bag 
	{ 
		[Constructable] 
		public HealBag() : this( 1 ) 
		{ 
		} 

		[Constructable] 
		public HealBag(int amount) 
		{ 
			Name = "CureBag";
			Hue = 33;

			DropItem( new GreaterHealPotion()); 
			DropItem( new GreaterHealPotion()); 
			DropItem( new GreaterHealPotion()); 
			DropItem( new GreaterHealPotion()); 
			DropItem( new GreaterHealPotion()); 
			DropItem( new GreaterHealPotion()); 
			DropItem( new GreaterHealPotion()); 
			DropItem( new GreaterHealPotion()); 
			DropItem( new GreaterHealPotion()); 
			DropItem( new GreaterHealPotion()); 
                        
                           
			



       
		} 

		public HealBag( Serial serial ) : base( serial ) 
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
