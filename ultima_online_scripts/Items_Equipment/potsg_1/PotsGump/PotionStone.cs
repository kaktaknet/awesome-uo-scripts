using System; 
using Server; 
using Server.Gumps; 
using Server.Network; 
using Server.Menus; 
using Server.Menus.Questions; 

namespace Server.Items 
{ 

   
   public class PotionStone : Item 
   {
	[Constructable] 
	public PotionStone() : base( 0xED4 ) 
	{
		Hue = 682;  
		Name = "PotionStone";
		Movable = false; 
	}
	public PotionStone( Serial serial ) : base( serial ) 
	{ 
	}
	public override void OnDoubleClick( Mobile from )

	{  
	if ( from.InRange( this.GetWorldLocation(), 2 ) ) 
	{ 
		from.SendGump( new PotionsGump( from ) ); 
	}
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
