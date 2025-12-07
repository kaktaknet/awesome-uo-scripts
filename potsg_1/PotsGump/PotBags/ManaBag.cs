//Original Bags By Dupre THANX!! *Ingot Bags*
//Edited to these Potion Bags For Full Sets In My Shard Dark Saints By Theron Of SOJ
using System; 
using Server; 
using Server.Items;

namespace Server.Items 
{ 
	public class ManaBag : Bag 
	{ 
		[Constructable] 
		public ManaBag() : this( 1 ) 
		{ 
		} 

		[Constructable] 
		public ManaBag(int amount) 
		{ 
			Name = "ManaBag";
			Hue = 1157;

			DropItem( new TotalManaRefreshPotion()); 
			DropItem( new TotalManaRefreshPotion()); 
			DropItem( new TotalManaRefreshPotion()); 
			DropItem( new TotalManaRefreshPotion()); 
			DropItem( new TotalManaRefreshPotion());
                        DropItem( new TotalManaRefreshPotion()); 
			DropItem( new TotalManaRefreshPotion()); 
			DropItem( new TotalManaRefreshPotion()); 
			DropItem( new TotalManaRefreshPotion()); 
			DropItem( new TotalManaRefreshPotion());
                        
                           
			



       
		} 

		public ManaBag( Serial serial ) : base( serial ) 
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
